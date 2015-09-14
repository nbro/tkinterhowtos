#!/usr/bin/env python3

"""
Author: Nelson Brochado

How to open a  window by specifying its coordinates with respect to the main window.
"""

import tkinter as tk


def on_click(root, x, y):
    second = tk.Toplevel(root)
    
    try:
        x = int(x)
        y = int(y)
        second.geometry('200x200+%d+%d' % (root.winfo_rootx() + x, root.winfo_rooty() + y))
    except ValueError:
        pass
    
    second.transient(root)    
    second.update_idletasks()  #  Updates second's coordinates.

    coords = tk.Label(second, text="Coordinates: x = %s, y = %s" % (second.winfo_rootx(), second.winfo_rooty()))
    coords.pack(expand=1, fill="both")

    coords = tk.Label(second, text="Root's coordinates: x = %s, y = %s" % (root.winfo_rootx(), root.winfo_rooty()))
    coords.pack(expand=1, fill="both")

    # Make second modal
    second.transient(root)
    second.grab_set()
    second.wait_window(second)


root = tk.Tk()

for i in range(2):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

label_x = tk.Label(root, text="Enter the difference in X: ")
label_x.grid(row=0, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

label_y = tk.Label(root, text="Enter the difference in Y: ")
label_y.grid(row=1, column=0)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

button_open = tk.Button(root, text="Open Second Window", command=lambda: on_click(root, entry_x.get(), entry_y.get()))
button_open.grid(row=2, column=1)

root.mainloop()
