# Chapter: Create Your Own Dialogs
# Description: class that derives from MyDialog of mydialog2.py
# File: mydialog3.py

import tkinter as tk

import mydialog2 as dialog


class MyDialog(dialog.MyDialog):
    def set_body(self, parent):
        self.name_label = tk.Label(parent, text="Name: ")
        self.name_label.pack(side='left', fill='both')
        self.name_entry = tk.Entry(parent)
        self.name_entry.pack(side='right', fill='both', pady=20)
        self.name_entry.focus()

    def validate(self):
        return True

    def apply(self, *args):
        print('Your name is', self.name_entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    dialog = MyDialog(root)
    root.mainloop()
