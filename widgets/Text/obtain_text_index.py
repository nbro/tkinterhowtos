#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

# Description

Example on how to find the index in a Text widget. Indexes are used to point to
positions within the text handled by the Text widget. Text widget indexes
correspond to positions between the actual characters.

# References

- https://stackoverflow.com/a/21680207/3924118
- http://effbot.org/tkinterbook/text.htm
"""

from tkinter import Tk, Frame, Text, Label


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.text = Text(self, wrap="word", font=("Helvetica", 18))
        self.text.insert("1.0", "Move your cursor around...")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.bind("<Any-Motion>", self.on_mouse_move)

        self.char = Label(self, text="Index:", bg="#ddd")
        self.char.pack(side="bottom", fill="x")

    def on_mouse_move(self, event):
        index = "Index: %s" % self.text.index("@%s,%s" % (event.x, event.y))
        self.char["text"] = index


if __name__ == "__main__":
    root = Tk()
    root.title("Example on how to find the index in a Text widget.")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
