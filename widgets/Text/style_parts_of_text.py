#!/usr/bin/env python3

"""
# Meta info

Author: Nelson Brochado

# Description

If you want to change the style of certain parts of text in a Text widget one
solution is to apply "tags" to the parts of text you want to customise.

You can create your tags using the method tag_configure, with a specific style,
and then you just need to apply this tag to the part of text you want to change
using the method tag_add. You can also remove the tags using the method
tag_remove.

The following example uses tag_configure, tag_add and tag_remove methods to
accomplish the goal just mentioned above.

# References

- http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_config-method
- http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_add-method
- http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_remove-method
- https://stackoverflow.com/a/30339009/3924118
"""

from tkinter import Tk, TclError, Frame, Button, Text
from tkinter.font import Font


class Example(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.toolbar = Frame(self, bg="#eee")
        self.toolbar.pack(side="top", fill="x")

        self.bold = Button(self.toolbar, text="Bold", command=self.make_bold)
        self.bold.pack(side="left")

        self.clear = Button(self.toolbar, text="Clear", command=self.clear)
        self.clear.pack(side="left")

        # Creates a bold font.
        self.bold_font = Font(family="Helvetica", size=14, weight="bold")

        self.text = Text(self)
        self.text.insert("end", "Select part of text and then click 'Bold'...")
        self.text.focus()
        self.text.pack(fill="both", expand=True)

        # Configures a tag called BOLD.
        self.text.tag_configure("BOLD", font=self.bold_font)

    def make_bold(self):
        # tk.TclError exception is raised if not text is selected.
        try:
            self.text.tag_add("BOLD", "sel.first", "sel.last")
        except TclError:
            pass

    def clear(self):
        self.text.tag_remove("BOLD", "1.0", 'end')


if __name__ == "__main__":
    root = Tk()
    Example(root).pack(expand=1, fill="both")
    root.mainloop()
