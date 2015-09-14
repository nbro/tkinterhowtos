#!/usr/bin/env python3

# opens a second window
# by specifying its coordinates
# with respect to the main window

# Author: Nelson Brochado

import tkinter as tk


def on_click(root, x, y):
    print("Root's coordinates:", root.winfo_rootx(), root.winfo_rooty())
    
    second_window = tk.Toplevel(root)

    try:
        x = int(x)
        y = int(y)
        second_window.geometry('+%d+%d' % (root.winfo_rootx() + x, root.winfo_rooty() + y))
    except ValueError:
        pass
    
    second_window.transient(root)    
    second_window.update_idletasks()  # coordinates of second window are updated
    print("Second Window's coordinates:", second_window.winfo_rootx(), second_window.winfo_rooty())

root = tk.Tk()

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
