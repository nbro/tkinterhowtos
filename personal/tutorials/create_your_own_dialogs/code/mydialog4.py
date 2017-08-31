# Chapter: Create Your Own Dialogs
# Description: Using the grid layout to create a dialog
# File: mydialog4.py

import tkinter as tk

import mydialog2 as dialog


class MyDialog(dialog.MyDialog):
    def set_body(self, parent):
        self.name_label = tk.Label(parent, text="Name: ")
        self.name_label.grid(row=0, column=0, sticky='w')
        self.name_entry = tk.Entry(parent)
        self.name_entry.grid(row=0, column=1)
        self.name_entry.focus()
        self.password_label = tk.Label(parent, text="Password: ")
        self.password_label.grid(row=1, column=0, sticky='w')
        self.pwd_entry = tk.Entry(parent, show='*')
        self.pwd_entry.grid(row=1, column=1)
        self.value = tk.IntVar(parent)

        # Using a lambda to change the property show of self.pwd_entry
        self.show_password = tk.Checkbutton(parent, variable=self.value, text='Show password',
                                            command=lambda: self.pwd_entry.config(
                                                show='')
                                            if self.value.get() == 1
                                            else self.pwd_entry.config(show='*'))
        self.show_password.grid(row=2, column=0)

    def validate(self):
        return True

    def apply(self, *args):
        print('Your name is:', self.name_entry.get())
        print('Your password is:', self.pwd_entry.get())


if __name__ == '__main__':
    root = tk.Tk()
    dialog = MyDialog(root)
    root.mainloop()
