"""
Applying tags to certain parts of text.

The main idea is to apply _tags_ to the parts of text you want to customise. You can create your tags using the method [`tag_configure`](http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_config-method), with a specific style, and then you just need to apply this tag to the part of text you want to change using the method [`tag_add`](http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_add-method).
You can also remove the tags using the method [`tag_remove`](http://effbot.org/tkinterbook/text.htm#Tkinter.Text.tag_remove-method).

The following is an example that uses `tag_configure`, `tag_add` and `tag_remove` methods.
"""

__author__ = "Nelson Brochado"
__version__ = "0.0.1"

#!/usr/bin/env python3

import tkinter as tk
from tkinter.font import Font

class Pad(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.toolbar = tk.Frame(self, bg="#eee")
        self.toolbar.pack(side="top", fill="x")

        self.bold_btn = tk.Button(self.toolbar, text="Bold", command=self.make_bold)
        self.bold_btn.pack(side="left")

        self.clear_btn = tk.Button(self.toolbar, text="Clear", command=self.clear)
        self.clear_btn.pack(side="left")

        # Creates a bold font
        self.bold_font = Font(family="Helvetica", size=14, weight="bold")

        self.text = tk.Text(self)
        self.text.insert("end", "Select part of text and then click 'Bold'...")
        self.text.focus()
        self.text.pack(fill="both", expand=True)

        # configuring a tag called BOLD
        self.text.tag_configure("BOLD", font=self.bold_font)

    def make_bold(self):
        # tk.TclError exception is raised if not text is selected
        try:
            self.text.tag_add("BOLD", "sel.first", "sel.last")        
        except tk.TclError:
            pass

    def clear(self):
        self.text.tag_remove("BOLD",  "1.0", 'end')


def demo():
    root = tk.Tk()
    Pad(root).pack(expand=1, fill="both")
    root.mainloop()


if __name__ == "__main__":
    demo()
