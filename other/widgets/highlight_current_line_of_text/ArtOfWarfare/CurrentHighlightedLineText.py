"""
Source: http://stackoverflow.com/questions/9691205/how-to-highlight-the-current-line-of-a-text-widget

Author: ArtOfWarfare
"""

import tkinter as tk


class CurrentHighlightedLineText(tk.Text):

    """Text widget with current line highlighted"""

    def __init__(self, root, *args, **kwargs):
        tk.Text.__init__(self, root, *args, **kwargs)

        self.tag_configure('currentLine', background='#e9e9e9')
        self.bind('<Key>', lambda _: self.highlightCurrentLine())
        self.bind('<Button-1>', lambda _: self.highlightCurrentLine())
        self.highlightCurrentLine(delay=0)

    def highlightCurrentLine(self, delay=10):

        def delayedHighlightCurrentLine():
            self.tag_remove('currentLine', 1.0, "end")
            self.tag_add('currentLine', 'insert linestart', 'insert lineend+1c')
        # This bound function is called before the cursor actually moves.
        # So delay checking the cursor position and moving the highlight 10 ms.

        self.after(delay, delayedHighlightCurrentLine)


if __name__ == "__main__":
    root = tk.Tk()

    text = CurrentHighlightedLineText(root)
    text.grid(row=0, column=0, sticky='nesw')

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
