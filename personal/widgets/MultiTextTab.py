"""
MultiTextTab 
Author: Nelson Brochado
Version: 0.0.1
"""

import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class TextTab(tk.Frame):

    def __init__(self, parent, tab_id, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.id = tab_id
        self.text = ScrolledText(self)
        self.text.pack(expand=1, fill="both")
                

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
        self.button_options = {"bd": 1, "relief": "groove", "padx": 15, "pady": 7, 
                               "font": ("Arial", 14), "activebackground": "#e1aaf4",
                               "activeforeground": "#156093", "bg": "white", "fg": "#11a3b5",
                               "state": "normal"}
        self.current_id = -1
        self.add()
        self.add()
        self.add()

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
        self.buttons[tab_id].config(state="active")
        
        if self.current_id == -1:
            self.tabs[tab_id].lift()            
        elif len(self.tabs) > 1 and self.current_id != tab_id:           
            self.tabs[self.current_id].lower()
            self.tabs[tab_id].lift()
            
        self.current_id = tab_id
        self.tabs[self.current_id].text.focus_set()
                           

def demo():
    root = tk.Tk()
    tabbed_pane = MultiTextTab(root)
    tabbed_pane.pack(expand=1, fill="both")
    root.mainloop()

if __name__ == "__main__":
    demo()
