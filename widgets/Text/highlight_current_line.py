#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

# Description

An example on how to highlight the current line in a Text widget while writing.

# References

- https://stackoverflow.com/a/9720858/3924118
"""

from tkinter import Tk, Frame, Text


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.text = Text(self)
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("current", background="#e9e9e9")

        self.highlight_current_line()

    def highlight_current_line(self, interval=50):
        self.text.tag_remove("current", 1.0, "end")
        self.text.tag_add("current", "insert linestart", "insert lineend+1c")
        self.after(interval, self.highlight_current_line)


if __name__ == "__main__":
    root = Tk()
    Example(root).pack()
    root.mainloop()
