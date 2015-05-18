"""
Source: http://stackoverflow.com/questions/19369391/how-to-draw-on-a-button-widget-or-how-to-make-a-button-out-of-a-canvas

Author: Bryan Oakley

Illusion of a circular Button created with a Canvas.
"""

import tkinter as tk
from tkinter import messagebox

class PseudoCircularButton(tk.Canvas):

    """Illusion of a circular Button created with a Canvas"""

    def __init__(self, parent, width, height, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,
                           relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding, padding, width + padding, height + padding),
                              outline=color, fill=color)
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0) + padding
        height = (y1 - y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


def callback():
    messagebox.showinfo("hello", "Hello World")


if __name__ == '__main__':
    master = tk.Tk()
    custom = PseudoCircularButton(master, 50, 50, 'red', command=callback)
    custom.pack()
    master.mainloop()
