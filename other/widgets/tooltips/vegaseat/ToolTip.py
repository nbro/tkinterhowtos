"""
Source: https://www.daniweb.com/software-development/python/code/484591/a-tooltip-class-for-tkinter
Description: Gives a Tkinter widget a tooltip as the mouse is above the widget
Language: Python 3
"""

import tkinter as tk

class ToolTip:

    """create a tooltip for a given widget"""

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        
        # Creates a Toplevel window for the actual tool tip
        self.tooltip = tk.Toplevel(self.widget)
        
        # Removes the Toplevel decorations (closing buttons...)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))

        # Will hold the message in the tool tip
        label = tk.Label(self.tooltip, text=self.text, justify='left', bg='#FFFFE0',
                         relief='solid', borderwidth=1)
        label.pack(ipadx=3, ipady=2)

    def close(self, event=None):
        """Removes the tooltip when the mouse is not over the widget"""
        if self.tooltip:
            self.tooltip.destroy()


if __name__ == '__main__':
    root = tk.Tk()

    btn = tk.Button(root, text='Enter!')
    btn.pack(side='left')

    entry = tk.Entry(root)
    entry.pack(side='left')
    
    ToolTip(btn, 'Tool tip for a Button widget')
    ToolTip(entry, 'Tool tip for a Entry widget')
    
    root.mainloop()
