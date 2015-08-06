"""
Source: http://forums.devshed.com/python-programming-11/syntax-highlighting-172406.html
Example of a syntax highlighting Text
"""

from tkinter import *
import keyword
from string import ascii_letters, digits, punctuation


class SyntaxHighlightingText(Text):

    tags = {'kw': 'orange', 'int': 'red'}

    def __init__(self, root):
        Text.__init__(self, root)
        self.config_tags()
        self.characters = ascii_letters + digits + punctuation
        self.bind('<Key>', self.key_press)

    def config_tags(self):
        for tag, val in self.tags.items():
            self.tag_config(tag, foreground=val)

    def remove_tags(self, start, end):
        for tag in self.tags.keys():
            self.tag_remove(tag, start, end)

    def key_press(self, key, delay=10):
        cline = self.index('insert').split('.')[0]
        lastcol = 0
        char = self.get('{0}.{1}'.format(cline, lastcol))
        while char != '\n':  # while we do not have a new line
            lastcol += 1
            char = self.get('{0}.{1}'.format(cline, lastcol))

        # get current line of text
        buffer = self.get('{0}.{1}'.format(cline, 0), '{0}.{1}'.format(cline, lastcol))

        # split the line into tokens
        tokenized = buffer.split(' ')

        # remove previous tags
        self.remove_tags('{0}.{1}'.format(cline, 0), '{0}.{1}'.format(cline, lastcol))
        start, end = 0, 0

        # iterate through the words of the line
        for token in tokenized:

            end = start + len(token)  # starting and ending index of each token
            # if it's a keyword, then add the tag to that keyword
            if token in keyword.kwlist:
                self.tag_add('kw', '{0}.{1}'.format(cline, start), '{0}.{1}'.format(cline, end))

            else:  # highlighting numbers
                for index in range(len(token)):
                    try:
                        int(token[index])
                    except ValueError:
                        pass
                    else:
                        self.tag_add('int', '{0}.{1}'.format(cline, start + index))

            start += len(token) + 1  # chaning starting index


if __name__ == '__main__':
    root = Tk()
    sht = SyntaxHighlightingText(root)
    sht.pack()
    root.mainloop()
