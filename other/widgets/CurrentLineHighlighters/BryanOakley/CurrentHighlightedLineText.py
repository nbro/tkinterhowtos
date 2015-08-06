"""
Source: http://stackoverflow.com/questions/9691205/how-to-highlight-the-current-line-of-a-text-widget

Author: Bryan Oakley
"""

import tkinter as tk


class CurrentHighlightedLineText(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.text = tk.Text(self)
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("current_line", background="#e9e9e9")

        self._highlight_current_line()

    def _highlight_current_line(self, interval=50):
        '''Updates the 'current line' highlighting every "interval" milliseconds'''
        self.text.tag_remove("current_line", 1.0, "end")
        self.text.tag_add("current_line", "insert linestart", "insert lineend+1c")
        self.after(interval, self._highlight_current_line)

if __name__ == "__main__": 
    app = CurrentHighlightedLineText()
    app.mainloop()
