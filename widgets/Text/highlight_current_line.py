#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

# Description

An example on how to highlight the current line in a Text widget while writing.

# References

- https://stackoverflow.com/a/9720858/3924118
- http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_add-method
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

        # insert is a named index and corresponds to the insertion cursor.
        #
        # Expressions can be used to modify any kind of index. Expressions are
        # formed by taking the string representation of an index, like "insert",
        # and appending one or more modifiers.
        #
        # In this case, we append the "linestart" modifier to "insert" as the
        # first index, and "lineend" and "+1c" to "insert" as last index.
        #
        # linestart moves the index to the first position on the line.
        #
        # lineend is the index to the last position on the line (the newline).
        #
        # +1c is an abbreviation of "+ 1 chars", and means to move the index
        # forward, which is moved over newlines, but not beyond the END index.
        self.text.tag_add("current", "insert linestart", "insert lineend+1c")
        self.after(interval, self.highlight_current_line)


if __name__ == "__main__":
    root = Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
