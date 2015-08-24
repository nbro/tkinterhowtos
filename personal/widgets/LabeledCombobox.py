"""
In this file you will find the LabeledCombobox widget,
which is basically a ttk.Combobox with a tkinter.Label attached.

You can associate a certain output
with a certain value of an item of the combobox,
by passing as argument a dictionary,
whose keys are the items of the combobox,
and the corresponding values are the values of the label.
"""

__author__ = "Nelson Brochado"


import tkinter as tk
from tkinter import ttk


class LabeledCombobox(tk.Frame):
    """LabeledCombobox is a ttk.Combobox with a tkinter.Label attached to it."""

    def __init__(self, master, dictionary, *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        self.dictionary = dictionary

        self.combo = ttk.Combobox(self, values=sorted(list(dictionary.keys())), state='readonly')
        self.combo.current(0)
        self.combo.pack(fill="both")
        self.combo.bind('<<ComboboxSelected>>', self.on_selection)

        self.label = tk.Label(self, text=self.value())
        self.label.pack(fill="both", expand=True)
        

    def value(self):
        return self.dictionary[self.combo.get()]

    def on_selection(self, event=None):  # Just to test
        self.label.config(text=self.value())
        

rgb = {"Red": "(256, 0, 0)", "Green": "(0, 256, 0)", "Blue": "(0, 0, 256)"}


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Labeled comboboxes")
    combo1 = LabeledCombobox(root, rgb, bd=0.5, relief="groove")
    combo1.pack(padx=(2, 2), pady=5)    
    root.mainloop()
