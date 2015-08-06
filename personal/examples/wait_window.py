"""
Example on how to use the "wait_window" function.

Author: Nelson Brochado
"""

import tkinter as tk
from tkinter import ttk


def create_new_window():
    
    dialog = tk.Toplevel()
    label = tk.Label(dialog, text="This is a toplevel window!")
    label.pack()

    if cb_state.get():
        dialog.wait_window(dialog)
        
        # this code is executed only when "dialog" is destroyed
        print("Dialog stopped waiting.")
    else:
        print("No mini-event loop happened.")


if __name__ == "__main__":
    root = tk.Tk()

    button_new_window = tk.Button(root, text='New Window', command=create_new_window)
    button_new_window.pack(side="left")

    cb_state = tk.IntVar()
    
    checkbutton_modal = ttk.Checkbutton(root, text="Wait Window", variable=cb_state)
    checkbutton_modal.pack(side="left")
    
    root.mainloop()
