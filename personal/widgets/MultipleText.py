"""
Multiple text widget with <Tab> event
make the focus switch between Text widgets

Author: Nelson Brochado
Based on a Bryan Oakley solution...

TODO:
- Possibility to turn to the previous Text widget
maybe with the usual keys shortcuts SHIFT + TAB
"""

import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class MultipleText(tk.Frame):
    """Widget with multiple Text widgets.
    Click tab to change from one Text widget to the other."""

    def __init__(self, parent, num_of_texts, *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)
        self.parent = parent
        self.texts = []
        for i in range(num_of_texts):
            self.texts.append(ScrolledText(m, width=30, height=20, bg='#333',
                                           fg="#10eeff", insertbackground="white"))
            self.texts[-1].pack(expand=1, fill='both', side='left')
            self.texts[-1].bind('<Tab>', self.on_tab_click)
        self.texts[0].focus()

    def on_tab_click(self, event=None):
        event.widget.tk_focusNext().focus()
        return 'break'


if __name__ == '__main__':
    m = tk.Tk()
    multiple_text = MultipleText(m, 3)
    m.mainloop()
