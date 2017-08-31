# Chapter: Create Your Own Dialogs
# Description: simple dialog derived from Toplevel
# File: mydialog.py

import tkinter as tk


class MyDialog(tk.Toplevel):
    def __init__(self, parent, message):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent

        self.label = tk.Label(self, text=message)
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack(padx=5)

        self.button = tk.Button(self, text="OK", command=self.ok)
        self.button.pack(pady=5)

    def ok(self):
        print("You entered: ", self.entry.get())
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    button = tk.Button(root, text='Click me')
    button.pack()
    dialog = MyDialog(parent=root, message='Enter something')
    root.wait_window(dialog)
