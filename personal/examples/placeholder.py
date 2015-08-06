"""
Simple placeholder for a password Entry widget.

Author: Nelson Brochado
Based on a Stack Overflow's post.
"""


import tkinter as tk


PLACEHOLDER = 'Enter your password...'

def on_focus_in(event):
    if event.widget.get() == PLACEHOLDER:
        event.widget.delete(0, "end")
        event.widget.config(show="*")

def on_focus_out(event):
    if event.widget.get() == "":
        event.widget.insert(0, PLACEHOLDER)
        event.widget.config(show="")


root = tk.Tk()

label = tk.Label(root, text="Password")
label.pack(side="left")

entry = tk.Entry(root, bd=1, show="")
entry.insert(0, PLACEHOLDER)
entry.bind('<FocusIn>', on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.pack(side="left")

button = tk.Button(root, text="Click me!")
button.pack(side="left")

root.mainloop()
