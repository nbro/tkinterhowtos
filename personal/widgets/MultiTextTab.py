"""
MultiTextTab - Tabbed Pane that supports tabs with Text widgets

Author: Nelson Brochado
Version: 0.0.1

TODO:
I have to redesign all the project.
I need to think which classes I need
and what are the best approach to implement them.

I should keep in mind always
that should minimise the dependencies between classes.

This MultiTexTab should support:
- Opening a new tab.
- Close a specific opened tab.
- Close all tabs (with optional prompt that can be specified in a settings file).
- Saving of the contents of the current tab (before quitting).
- Opening file and write it in the Text widget.
- Saving the contents of all opened tabs.
- Rename the new tab (default name of the associated file).
- Erase content of text widget.
"""

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from collections import OrderedDict as OD

# TODO
# Maybe a OptionMenu object is not so indicative for this case
class TabOptionMenu(tk.Frame):

    """Menu that pops up with all the options regarding a TextTab or the MultiTexTab."""
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.options = OD([("New tab", self.new_tab),
                           ("Close tab", self.close_tab),
                           ("Close all", self.close_all),
                           ("Save", self.save),
                           ("Save all", self.save_all),
                           ("Open file", self.open_file),
                           ("Rename", self.rename),
                           ("Erase", self.erase)])
        
        self.buttons = { }

    def _create_buttons(self):
        """Creates buttons with bindings
        and associates each of them with the corresponding operation."""
        pass
        

    def new_tab(self, event=None):
        pass
    
    def close_tab(self, event=None):
        pass
    
    def close_all(self, event=None):
        pass
    
    def save(self, event=None):
        pass
    
    def save_all(self, event=None):
        pass
    
    def open_file(self, event=None):
        pass
    
    def rename(self, event=None):
        pass
    
    def erase(self, event=None):
        pass
    
def test1():
    r = tk.Tk()
    tb = TabOptionMenu(r)
    tb.pack()
    r.mainloop()

# test1()


# TODO
class TabButton(tk.Frame):

    """Button associated with a TextTab object"""
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # JUST A SIMPLE TEST...
        self.label = tk.Label(self, text="Page 1")
        self.label.pack(expand=1, fill="both", side="left", padx=6, pady=3)

        self.closer = tk.Button(self, text="", width=0)
        self.closer.pack(fill="both", side="left")

        self.config(bd=1, relief="groove")
        

def test_TabButton():
    r = tk.Tk()
    tb = TabButton(r)
    tb.pack()
    
    r.mainloop()

# test_TabButton()

# NEEDS NEW DESIGN
class TextTab(tk.Frame):
    def __init__(self, parent, tab_id, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.id = tab_id
        self.text = ScrolledText(self)
        self.text.pack(expand=1, fill="both")
                              

# NEEDS NEW DESIGN
class MultiTextTab(tk.Frame):

    """MultiTextTab widget"""

    def __init__(self, parent, tab_name="Page ", *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tab_name = tab_name
                
        self.top = tk.Frame(self, bg="#eee")
        self.top.pack(side="top", fill="x")

        self.body = tk.Frame(self, bg="#ddd")
        self.body.pack(fill="both", expand=True)
        self.body.grid_columnconfigure(0, weight=1)
        self.body.grid_rowconfigure(0, weight=1)
    
        self.tabs = {}
        self.buttons = {}
        self.button_options = {"bd": 1, "relief": "groove", "padx": 15, "pady": 6, 
                               "font": ("Arial", 13), "activebackground": "#e1aaf4",
                               "activeforeground": "#156093", "bg": "white", "fg": "#11a3b5",
                               "state": "normal"}
        self.current_id = -1

    def reset(self):
        for v in self.buttons.values():
            v.config(**self.button_options)

    def add(self):
        tab = TextTab(self.body, len(self.tabs) + 1)
        tab.grid(row=0, column=0, sticky="nsew")
        
        button = tk.Label(self.top, text=self.tab_name + str(tab.id), **self.button_options)
        button.bind("<Button-1>", lambda e: self.raise_tab(e, tab.id))
        button.pack(side="left", fill="both", padx=2, pady=2)

        self.buttons[tab.id] = button
        
        self.tabs[tab.id] = tab        
        self.raise_tab(None, tab.id)

    def raise_tab(self, event, tab_id):
        self.reset()
        self.buttons[tab_id].config(state="active", font=("Arial", 13, "bold"))
        
        if self.current_id == -1:
            self.tabs[tab_id].lift()            
        elif len(self.tabs) > 1 and self.current_id != tab_id:           
            self.tabs[self.current_id].lower()
            self.tabs[tab_id].lift()
            
        self.current_id = tab_id
        self.tabs[self.current_id].text.focus_set()


def make_topmost(m):
    """m is a Toplevel or a Tk widget"""
    m.lift()
    m.attributes("-topmost", 1)
    m.attributes("-topmost", 0)
    

def demo():
    root = tk.Tk()
    make_topmost(root)
    tabbed_pane = MultiTextTab(root)
    tabbed_pane.add()
    tabbed_pane.add()
    tabbed_pane.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    demo()
