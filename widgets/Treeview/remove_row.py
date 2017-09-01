#!/usr/bin/env python3

"""
# Meta info

Author: Nelson Brochado

# Description

Simple example on how to delete a row from a Treeview.

# References

- http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Treeview.html
"""

from tkinter import Tk, Button, Frame
from tkinter.ttk import Treeview


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.tree = Treeview(self)

        self.tree["columns"] = ("item1", "item2")
        self.tree.heading("item1", text="Column 1")
        self.tree.heading("item2", text="Column 2")

        self.tree.insert("", 0, text="Item 1", values=("Value 1", "Value 2"))

        row2 = self.tree.insert("", 1, "row2", text="Item 2")
        self.tree.insert(row2, "end", "item1", text="Item 1", values=("3", "7"))
        self.tree.insert(row2, "end", "item2", text="Item 2", values=("2", "5"))

        self.tree.pack(expand=1, fill="both")

        self.delete = Button(self, text="Delete Row", command=self.on_delete)
        self.delete.pack(side="bottom")

    def on_delete(self):
        try:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)
        except IndexError:
            pass


if __name__ == "__main__":
    root = Tk()
    root.title("Simple example on how to delete a row from a Treeview.")
    Example(root).pack(expand=1, fill="both")
    root.mainloop()
