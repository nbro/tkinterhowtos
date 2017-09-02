#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta info

Author: Nelson Brochado

# Description

An example on how to change the contents of one OptionMenu based on the selected
option of another OptionMenu.

# References

http://effbot.org/tkinterbook/variable.htm
https://stackoverflow.com/a/5636417/3924118
https://stackoverflow.com/a/17252390/3924118
"""

from tkinter import Tk, Frame, StringVar, OptionMenu


class Example(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.dict = {'Asia': ['Japan', 'China', 'India'],
                     'Europe': ['Portugal', 'Switzerland', 'Ukraine']}

        self.var_a = StringVar(self)
        self.var_b = StringVar(self)

        self.var_a.trace('w', self.update_options)

        self.option_menu_a = OptionMenu(self, self.var_a, *self.dict.keys())
        self.option_menu_a.pack(side="top")
        self.option_menu_a["width"] = 10
        self.option_menu_b = OptionMenu(self, self.var_b, '')
        self.option_menu_b["width"] = 10
        self.option_menu_b.pack(side="top")

        self.var_a.set('Asia')

    def update_options(self, *args):
        countries = self.dict[self.var_a.get()]
        self.var_b.set(countries[0])

        menu = self.option_menu_b['menu']
        menu.delete(0, 'end')

        for c in countries:
            menu.add_command(label=c, command=lambda x=c: self.var_b.set(x))


if __name__ == "__main__":
    root = Tk()
    Example(root).pack(expand=True, fill="both")
    root.mainloop()
