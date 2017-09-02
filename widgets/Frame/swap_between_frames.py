#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

# Description

A famous example on how to swap between frames that are on top of each other.
Frames are stacked on top of each other using the "grid" package manager.

# References

- https://stackoverflow.com/a/7557028/3924118
- https://stackoverflow.com/a/31603579/3924118
- https://stackoverflow.com/a/7591453/3924118
"""

from random import randint, randrange
from tkinter import Tk, Frame, Label, Button


def rand_hex_color():
    return '#%02X%02X%02X' % (randint(0, 255), randint(0, 255), randint(0, 255))


class Example(Frame):
    def __init__(self, master, n=10):
        Frame.__init__(self, master)

        assert n > 1

        # Makes frames resize when window resizes.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.create_frames(n)
        self.fill_frames(n)
        self.frames[randrange(0, n)].tkraise()

    def create_frames(self, n):
        for i in range(n):
            self.frames[i] = Frame(self, bg=rand_hex_color())
            self.frames[i].grid(row=0, column=0, sticky='nsew')

    def fill_frames(self, n):
        for i in range(n):
            label = Label(self.frames[i], text='Frame %d' % i)
            label.pack(side="top", padx=10, pady=(10, 10))

            button = Button(self.frames[i],
                            text='Go to frame %d' % ((i + 1) % n),
                            command=lambda x=(i + 1) % n:
                            self.frames[x].tkraise())
            button.pack(side="bottom", padx=10, pady=(0, 10))


if __name__ == "__main__":
    root = Tk()
    Example(root).pack(expand=True, fill="both")
    root.mainloop()
