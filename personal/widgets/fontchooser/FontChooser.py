"""
Author: Nelson Brochado
Creation: End of 2014
Last Update: 9.05.2015

Description:
This file contains the needed classes for the FontChooser class,
in addition of course to the FontChooser class.

Unless you have a specific reason, from this module
you should just call the function:

    askfont(parent)
    
where 'parent' should be a top level window
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font
import sys

import util


class ScrolledList(tk.Listbox):

    """Listbox with a vertical scrollbar
    for the class FontFamilies"""

    def __init__(self, master=None, cnf={}, **options):
        tk.Listbox.__init__(self, master, cnf, **options)
        self.scrollbar = tk.Scrollbar(master)
        self.show_scrollbar()
        # self calls self.scrollbar.set when the self's view is changed
        self.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.yview)

    def hide_scrollbar(self):
        self.scrollbar.pack_forget()

    def show_scrollbar(self):
        self.scrollbar.pack(side='right', fill='y')
        


class FontFamilies(tk.Frame):

    """represents a frame with a listbox of available fonts"""

    def __init__(self, parent, show_example=True, *args, **options):
        """if show_example is set to False,
        then an example of the current selected font is not shown"""
        tk.Frame.__init__(self, parent, *args, **options)
        
        self.title = tk.Label(self, text='Font Families', borderwidth=1, relief='groove', pady=2)
        self.title.pack(fill='x', pady=2)

        self.families = ScrolledList(self, exportselection=False)
        self.names = sorted(font.families())
        self.add_fonts()
        self.current_font = 'Courier New'
        self.set_selected_font(self.current_font)
        self.families.pack(expand=1, fill='both')
        
        self.example = tk.Entry(self, font=(self.selected_item(), 16))
        self.example.insert(0, 'Hello World')        
        if show_example:
            self.example.pack(fill='x', side='bottom')

        self.families.bind('<<ListboxSelect>>', lambda e: self.example.config(font=(self.selected_item(), 16)))

    def add_fonts(self):
        """you should not call this method except in the __init__ method"""
        for f in self.names:
            self.families.insert('end', f)

    def set_selected_font(self, font_name='Helvetica'):
        """if font_name is not present in font.families(),
        then no selection is done"""
        if font_name in self.names:
            font_index = self.names.index(font_name)
            self.families.select_set(font_index)
            self.families.see(font_index)

    def selected_item(self):
        """returns the selected item string"""
        return self.families.get(self.selected_index())

    def selected_index(self):
        """returns the index of the selected item.
        if not item is selected, it returns 0"""
        if len(self.families.curselection()):
            return self.families.curselection()[0]
        else:
            return 0


class FontSizes(tk.Frame):

    """Frame containing a combobox with available sizes for a font"""

    def __init__(self, parent=None, *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)
        self.title = tk.Label(self, text='Font Sizes', borderwidth=1, relief='groove', pady=2)
        self.title.pack(fill='x', pady=2)
        self.sizes = ttk.Combobox(self, state='readonly')
        self.add_sizes()
        self.sizes.pack(expand=1, fill='x')

    def add_sizes(self):
        self.sizes['values'] = util.FONT_SIZES
        self.sizes.current(11)


class FontStyles(tk.Frame):

    """Contains check buttons for styling the font"""

    def __init__(self, parent=None, **options):
        tk.Frame.__init__(self, parent, **options)
        
        self.title = tk.Label(self, text='Font Styles', borderwidth=1, relief='groove', pady=2)
        self.title.grid(row=0, column=0, sticky='new', pady=2)
        
        self.bold = tk.Checkbutton(self, text='Bold')
        self.bold.grid(row=1, column=0, sticky='w')
        
        self.italic = tk.Checkbutton(self, text='Italic')
        self.italic.grid(row=2, column=0, sticky='w')
        
        self.underline = tk.Checkbutton(self, text='Underline')
        self.underline.grid(row=3, column=0, sticky='w')
        
        self.overstrike = tk.Checkbutton(self, text='Overstrike')
        self.overstrike.grid(row=4, column=0, sticky='w')
        
        # list containing references to the Checkbuttons
        # used for checks
        self.styles = [self.bold, self.italic, self.underline, self.overstrike]
        self.vars = []
        
        self.fill_vars()
        self.set_rows_weight()
        self.set_columns_weight()

    def fill_vars(self):
        for i in range(len(self.styles)):
            var = tk.IntVar()
            self.vars.append(var)
            self.styles[i].config(variable=var)

    def set_rows_weight(self, w=1):
        """private method"""
        for row in range(1, len(self.styles) + 1):
            self.rowconfigure(row, weight=w)

    def set_columns_weight(self, w=1):
        """private method"""
        self.columnconfigure(0, weight=w)


class FontBody(tk.Frame):

    """Font body of a font chooser object"""

    def __init__(self, parent, example=True, *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)
        self.parent = parent

        self.families = FontFamilies(self, show_example=example)
        self.families.pack(fill='y', side='left', padx=1, pady=1)

        self.styles = FontStyles(self)
        self.styles.pack(expand=1, fill='both', side='top', padx=1, pady=1)
        
        self.sizes = FontSizes(self)
        self.sizes.pack(fill='x', side='bottom', padx=1, pady=1)

    def current_font(self):
        """returns the font built of the current selected family
        style and size."""
        current_weight = 'bold' if self.styles.vars[0].get() else 'normal'
        current_italic = 'italic' if self.styles.vars[1].get() else 'roman'
        current_underline = self.styles.vars[2].get()
        current_overstrike = self.styles.vars[3].get()

        f = font.Font(family=self.families.selected_item(), weight=current_weight, slant=current_italic,
                      size=self.sizes.sizes.get(), underline=current_underline, overstrike=current_overstrike)
        return f
    

class FontFooter(tk.Frame):

    """Bottom bar for the font chooser"""

    def __init__(self, parent, font_body, *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)
        self.parent = parent
        self.font_body = font_body
        self.ok = tk.Button(self, text='Ok', command=self.ok, font=('Arial', 12, 'bold'))
        self.ok.pack(side='right', padx=5, ipady=3)
        
        self.cancel = tk.Button(self, text='Cancel', command=self.cancel)
        self.cancel.pack(side='right', padx=5)

    def current_font(self):
        return self.font_body.current_font()

    def ok(self):
        self.parent.font = self.current_font()
        self.parent.destroy()

    def cancel(self):
        self.parent.font = None
        self.parent.destroy()


class FontChooser(tk.Toplevel):

    """represents a window with a list of fonts to choose"""

    def __init__(self, parent, *args, **options):
        tk.Toplevel.__init__(self, parent, *args, **options)
        self.title("Font Chooser")
        
        self.font = None  # will hold the font
        
        self.body = FontBody(self)
        self.body.pack(expand=1, fill='both', side='top', padx=2)
        self.footer = FontFooter(self, self.body, borderwidth=1, relief='groove')
        self.footer.pack(fill='x', side='bottom', padx=3, pady=2)

        self.focus()
        self.grab_set()  # grab all events and direct them toward this window
        self.protocol('WM_DELETE_WINDOW', self.destroy)

    def show(self):
        self.wm_deiconify()
        self.wait_window()
        return self.font


# READ: http://effbot.org/tkinterbook/tkinter-dialog-windows.htm
def askfont(parent):
    return FontChooser(parent).show()

    
def main():    
    root = tk.Tk()

    # the following 2 lines
    # prevent the text widget from resizing
    # when changing the font
    root.pack_propagate(False)
    root.geometry("500x400+200+200")
    util.make_topmost(root)
    
    text = tk.Text(root)
    text.focus()
    text.pack(expand=1, fill='both')

    chooser = tk.Button(root, text="Choose font", command=lambda: text.config(font=askfont(root)))
    chooser.pack(side="bottom")
    
    root.mainloop()
    
if __name__ == '__main__':
    main()

