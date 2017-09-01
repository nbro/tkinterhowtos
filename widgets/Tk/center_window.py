#!/usr/bin/env python3

"""
# Meta info

Author: Nelson Brochado

# Description

Center a Tk window by directly executing a Tk command.

# References

- https://stackoverflow.com/a/28224382/3924118
"""

from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    root.eval(
        'tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    root.mainloop()
