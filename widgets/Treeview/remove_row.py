#!/usr/bin/env python3

"""
# Meta info

Author: Nelson Brochado

# Description

Simple example on how to delete a row from a Treeview.
"""

from tkinter import Tk, Button, ttk, Frame


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.tree = ttk.Treeview(self)

        self.tree["columns"] = ("item1", "item2")
        self.tree.heading("item1", text="Column 1")
        self.tree.heading("item2", text="Column 2")

        self.tree.insert("", 0, text="Item 1", values=("Value 1", "Value 2"))

        row2 = self.tree.insert("", 1, "row2", text="Item 2")
        self.tree.insert(row2, "end", "index1", text="Item 1",
                         values=("Value 1", "Value 2"))
        self.tree.insert(row2, "end", "index2", text="Item 2",
                         values=("Value 1", "Value 2"))
        self.tree.insert(row2, "end", "index3", text="Item 3",
                         values=("Value 1", "Value 2"))

        self.tree.pack(expand=1, fill="both")

        self.delete = Button(self, text="Delete", command=self.on_delete)
        self.delete.pack(side="bottom")

    def on_delete(self):
        try:
            selected_item = self.tree.selection()[0]  # Get selected item
            self.tree.delete(selected_item)
        except IndexError:
            pass


if __name__ == "__main__":
    root = Tk()
    root.title("Simple example on how to delete a row from a Treeview.")
    Example(root).pack(expand=1, fill="both")
    root.mainloop()
