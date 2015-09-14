"""
Author: Nelson Brochado
"""

import tkinter as tk
import webbrowser


class HyperlinkLabel(tk.Label):

    """Hyperlink label that accepts a url of a webpage to be open
    when the text of the label is clicked."""

    def __init__(self, parent, linktext="Hyperlink", href="", *args, **kwargs):
        tk.Label.__init__(self, parent, text=linktext, cursor="hand2", relief="sunken",
                          bd=1, padx=10, pady=5, *args, **kwargs)

        self.normal_color = "#00aaff"
        self.hover_color = "#00eeff"
        self.visited_color = "#0033ff"
        
        self.config(fg=self.normal_color)
        
        self.href = href
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.clicks = 0

    def on_enter(self, event=None):
        self.config(fg=self.hover_color)

    def on_leave(self, event=None):
        if self.clicks > 0:
            self.config(fg=self.visited_color)
        else:
            self.config(fg=self.normal_color)
        
    def on_click(self, event=None):
        self.clicks += 1
        webbrowser.open_new(self.href)

def main():
    root = tk.Tk()
    for i in range(5):
        link = HyperlinkLabel(root, href=r"https://www.google.ch", linktext="Google")
        link.pack(side="top", fill="x", padx=5, pady=3)

    closer = tk.Button(root, text="Close", command=root.destroy)
    closer.pack(side="top", fill="x", padx=5, pady=(8, 1))
        
    root.mainloop()

if __name__ == "__main__":
    main()
