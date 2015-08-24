"""A directory browser using Ttk Treeview.

Based on the demo found in Tk 8.5 library/demos/browse
"""

#author: unknown

import os
import glob
import tkinter as tk
from tkinter import ttk


class DirBrowser(tk.Toplevel):

    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        
        self.vsb = ttk.Scrollbar(self, orient="vertical")
        self.hsb = ttk.Scrollbar(self, orient="horizontal")

        self.tree = ttk.Treeview(self, columns=("fullpath", "type", "size"), displaycolumns="size",
                                 yscrollcommand=lambda f, l: self.autoscroll(self.vsb, f, l),
                                 xscrollcommand=lambda f, l: self.autoscroll(self.hsb, f, l))

        self.vsb['command'] = self.tree.yview
        self.hsb['command'] = self.tree.xview
        self.tree.grid(column=0, row=0, sticky="nsew")

        self.tree.heading("#0", text="Directory Structure", anchor='w')
        self.tree.heading("size", text="File Size", anchor='w')
        self.tree.column("size", stretch=0, width=100)

        self.populate_roots(self.tree)
        self.tree.bind('<<TreeviewOpen>>', self.update_tree)
        self.tree.bind('<Double-Button-1>', self.change_dir)
        
        self.vsb.grid(column=1, row=0, sticky='ns')
        self.hsb.grid(column=0, row=1, sticky='ew')        

    def populate_tree(self, tree, node):
        if tree.set(node, "type") != 'directory':
            return

        path = tree.set(node, "fullpath")
        tree.delete(*tree.get_children(node))

        parent = tree.parent(node)
        special_dirs = [] if parent else glob.glob('.') + glob.glob('..')

        for p in special_dirs + os.listdir(path):
            ptype = None
            p = os.path.join(path, p).replace('\\', '/')
            if os.path.isdir(p):
                ptype = "directory"
            elif os.path.isfile(p):
                ptype = "file"

            fname = os.path.split(p)[1]
            id = tree.insert(node, "end", text=fname, values=[p, ptype])

            if ptype == 'directory':
                if fname not in ('.', '..'):
                    tree.insert(id, 0, text="dummy")
                    tree.item(id, text=fname)
            elif ptype == 'file':
                size = os.stat(p).st_size
                tree.set(id, "size", "%d bytes" % size)

    def populate_roots(self, tree):
        dir = os.path.abspath('.').replace('\\', '/')
        node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
        self.populate_tree(tree, node)

    def update_tree(self, event):
        tree = event.widget
        self.populate_tree(tree, tree.focus())

    def change_dir(self, event):
        tree = event.widget
        node = tree.focus()
        if tree.parent(node):
            path = os.path.abspath(tree.set(node, "fullpath"))
            if os.path.isdir(path):
                os.chdir(path)
                tree.delete(tree.get_children(''))
                self.populate_roots(tree)

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)


if __name__ == "__main__":
    root = tk.Tk()
    opener = tk.Button(root, text="Open Directories' Browser",
                       command=lambda: DirBrowser(root))
    opener.pack()
    root.mainloop()
