"""
Author: Nelson Brochado
Creation: 01.01.2015
Last update: 11.05.2015

In this file you can find 3 classes:

 - TextPositionIndicator
 - IndicatorBottomBar
 - IndicatorText
 
See docstrings for more information.
"""

from tkinter import *


class TextPositionIndicator(Frame):
    """This class represents a line and character indicator of a Text widget"""

    L = 'Current line: '
    C = 'Current char: '
    LINES = 'Total lines: '
    CHARS = 'Total chars: '
    FONT = ("Calibri", 12)

    def __init__(self, parent, *args, **options):
        Frame.__init__(self, parent, *args, **options)
        # will hold reference to either a Text widget
        self.text = None
        # total get_lines and get_chars
        self.total_chars = self.total_lines = 0
        self.style = {"relief": 'groove', "bd": 1, "padx": 10, "pady": 2, "font": self.FONT}
        self.chars_label = Label(self, text=self.CHARS + str(self.total_chars), **self.style)
        self.lines_label = Label(self, text=self.LINES + str(self.total_lines), **self.style)
        self.chars_label.pack(side='right', fill='both')
        self.lines_label.pack(side='right', fill='both')
        # current line and char
        self.char = 0
        self.line = 1
        self.char_label = Label(self, text=self.C + str(self.char), **self.style)
        self.char_label.pack(side='right', fill='both')
        self.line_label = Label(self, text=self.L + str(self.line), **self.style)
        self.line_label.pack(side='right', fill='both')

    def reset(self):
        """Called to reset variables for counting get_lines and get_chars"""
        self.line = 1
        self.char = self.total_chars = self.total_lines = 0
        self.line_label.config(text=self.L + str(self.line))
        self.char_label.config(text=self.C + str(self.char))
        self.lines_label.config(text=self.LINES + str(self.total_lines))
        self.chars_label.config(text=self.CHARS + str(self.total_chars))

    def attach(self, text):
        """Text must be a Text widget object"""
        self.text = text
        self.text.bind('<KeyRelease>', lambda e: self.update(e))
        self.reset()

    def get_lines(self):
        """Returns the total number of get_lines in self.text.
        if self.text is None, it returns 0."""
        return len(self.text.get(1.0, 'end-1c').split('\n')) if self.text is not None else 0

    def get_chars(self):
        """Returns the total number of characters in self.text.
        new get_lines '\n' are not considered characters.
        if self.text is None, it returns 0"""
        chars = 0
        if self.text is not None:
            lines = self.text.get(1.0, 'end').split('\n')
            for line in lines:
                chars += len(line)
        return chars

    def update(self, event=None):
        """called when a key is release in a Text widget"""
        cursor_position = self.text.index('insert')
        self.line = int(cursor_position.split('.')[0])
        self.char = int(cursor_position.split('.')[1])
        self.total_lines = self.get_lines()
        self.total_chars = self.get_chars()
        self.line_label.config(text=self.L + str(self.line))
        self.char_label.config(text=self.C + str(self.char))
        self.lines_label.config(text=self.LINES + str(self.total_lines))
        self.chars_label.config(text=self.CHARS + str(self.total_chars))


class IndicatorBottomBar(Frame):
    """Bottom bar with a TextPositionIndicator"""

    def __init__(self, parent, *args, **options):
        Frame.__init__(self, parent, *args, **options)
        self.indicator = TextPositionIndicator(self)
        self.indicator.pack(fill='both', side='right')

    def attach(self, text_widget):
        self.indicator.attach(text_widget)


class IndicatorText(Frame):
    """Text widget with a IndicatorBottomBar"""

    def __init__(self, parent, *args, **options):
        Frame.__init__(self, parent, *args, **options)

        self.topframe = Frame(self, height=500)
        self.text = Text(self.topframe)
        self.text.focus()
        self.text.pack(expand=1, fill="both")
        self.bottom = IndicatorBottomBar(root)
        self.bottom.attach(self.text)
        self.bottom.pack(side="bottom", fill="x")
        self.topframe.pack(expand=1, fill="both", side="top")


if __name__ == '__main__':
    root = Tk()
    indicator = IndicatorText(root)
    indicator.pack(expand=1, fill="both")
    root.mainloop()
