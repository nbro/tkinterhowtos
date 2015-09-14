"""
Author: Nelson Brochado
Creation: February, 2015
Last update: 7.08.2015

Highlighting Engine to be used with 'Text' widgets or derived classes,
and to be used with objects of type 'Language' (found in 'lang/language.py')
HE uses some functions of the SE engine.
"""

import sys
from tkinter import Text, Tk
from se import *
from lang.language import *


class HE(object):

    """Highlighting Engine"""

    def __init__(self, text_widget, language, *args, **options):
        """
        :param text_widget => Text widget or derived objects
        :param language => object of type Language
        """
        self.language = language
        self.text_widget = text_widget
        self.start()

    def start(self):
        """Starts highlighting"""
        self.text_widget.config(fg=self.language.normal['fg'], bg=self.language.normal['bg'],
                                font=self.language.normal['font'])
        self.configure_tags()
        self.highlight_all(None)
        # binding on KeyRelease avoids the problem of coloring
        # only after we type another character after the word/expression
        # that should already be colored.
        self.text_widget.bind('<KeyRelease>', lambda e: self.highlight_current_line(e))

    def remove_tags(self, start='1.0', end='end-1c'):
        """
        Removes all tags associated with the current 'self.language' from the current 'self.text_widget'.
        :param start => index from where to start removing tags
        :param end => last index to look up to remove tags
        """
        for key in self.language.syntax.keys():
            self.text_widget.tag_remove(self.language.name + '_' + key, start, end)

    def last_column(self, line):
        """Returns a number representing the last column of 'line'"""
        last = 0
        char = self.text_widget.get('{}.{}'.format(line, last))
        while char != '\n':
            last += 1
            char = self.text_widget.get('{}.{}'.format(line, last))
        return last

    def line_text(self, line):
        """Returns the text of the line passed as argument"""
        return self.text_widget.get('{}.{}'.format(line, 0),
                                    '{}.{}'.format(line, self.last_column(line)))

    def configure_tags(self):
        for name, d in self.language.syntax.items():
            self.text_widget.tag_configure(d['tag'], foreground=d['fg'],
                                           background=d['bg'], font=d['font'])

    def highlight_all(self, event=None):
        """
        :keyword d => dictionary of values for name
        :keyword name => each possible key of 'self.language.syntax'
        """
        for name, d in self.language.syntax.items():
            if d['search'] == Language.SEARCH[0]:  # search words
                self.highlight_all_words(d['tag'], d['value'])
            elif d['search'] == Language.SEARCH[1]:  # search occurrences
                self.highlight_all_occurrences(d['tag'], d['value'])
            # search regular expressions
            elif d['search'] == Language.SEARCH[2]:
                self.highlight_all_regexps(d['tag'], d['value'])

    def highlight_all_words(self, tag, list_of_words):
        """Highlights all whole words that are not a regular expression"""
        text = self.text_widget.get(1.0, 'end-1c')
        lines = text.split('\n')
        for i in range(len(lines)):
            words = lines[i].split(' ')
            self.text_widget.tag_remove(tag, '{}.{}'.format(i + 1, 0),
                                        '{}.{}'.format(i + 1, self.last_column(i + 1)))
            first, last = 0, 0  # indexes of first and last character of words
            for word in words:
                last = first + len(word)
                if word in list_of_words:
                    self.text_widget.tag_add(tag, '{}.{}'.format(i + 1, first),
                                             '{}.{}'.format(i + 1, last))
                first += len(word) + 1  # passing to the next word

    def highlight_all_occurrences(self, tag, list_of_occurrences):
        """Highlights all (overlapping) occurrences of all items of 'list_of_occurrences'."""
        text = self.text_widget.get(1.0, 'end-1c')
        lines = text.split('\n')
        for i in range(len(lines)):
            occurrences = []
            for o in list_of_occurrences:
                for pair in SE.occurrences(o, lines[i]):
                    occurrences.append(pair)
            self.text_widget.tag_remove(tag, '{}.{}'.format(i + 1, 0),
                                        '{}.{}'.format(i + 1, self.last_column(i + 1)))
            for o in occurrences:
                self.text_widget.tag_add(tag, '{}.{}'.format(i + 1, o[0]),
                                         '{}.{}'.format(i + 1, o[1]))

    def highlight_all_regexps(self, tag, regexp):
        """Highlights all regular expressions matching regexp"""
        text = self.text_widget.get(1.0, 'end-1c')
        lines = text.split('\n')
        for i in range(len(lines)):
            occurrences = SE.occurrences_re(regexp, lines[i])
            self.text_widget.tag_remove(tag, '{}.{}'.format(i + 1, 0),
                                        '{}.{}'.format(i + 1, self.last_column(i + 1)))
            for o in occurrences:
                self.text_widget.tag_add(tag, '{}.{}'.format(i + 1, o[0]),
                                         '{}.{}'.format(i + 1, o[1]))

    def highlight_current_line(self, event=None):
        """Highlights all the words, occurrences or regular expressions that match the syntax of self.language."""
        for name, d in self.language.syntax.items():
            if d['search'] == Language.SEARCH[0]:  # search words
                self.highlight_words(d['tag'], d['value'])
            elif d['search'] == Language.SEARCH[1]:  # search words
                self.highlight_occurrences(d['tag'], d['value'])
            elif d['search'] == Language.SEARCH[2]:  # search words
                self.highlight_re(d['tag'], d['value'])
        self.text_widget.tag_raise("sel")
        # MAKES SELECTION WORK CORRECTLY:
        # http://stackoverflow.com/questions/1515809/how-to-remove-existing-background-color-of-text-when-highlighting?rq=1
        # http://stackoverflow.com/questions/23289214/tkinter-text-tags-select-user-highlight-colour/23293446#23293446

    def highlight_words(self, tag, list_of_words):
        """Highlights all the words of the current line
        that match any of the items in 'list_of_words'"""
        index = self.text_widget.index('insert').split('.')[0]
        line = self.line_text(index)
        words = line.split()
        self.text_widget.tag_remove(tag, '{}.{}'.format(index, 0),
                                    '{}.{}'.format(index, self.last_column(index)))
        first, last = 0, 0  # indexes of first and last character of words
        for word in words:
            last = first + len(word)
            if word in list_of_words:
                self.text_widget.tag_add(tag, '{}.{}'.format(index, first),
                                         '{}.{}'.format(index, last))
            first += len(word) + 1

    def highlight_occurrences(self, tag, list_of_occurrences):
        """Highlights all (overlapping) occurrences of all items of 'list_of_occurrences' of the current line."""
        index = self.text_widget.index('insert').split('.')[0]
        line = self.line_text(index)
        self.text_widget.tag_remove(tag, '{}.{}'.format(index, 0),
                                    '{}.{}'.format(index, self.last_column(index)))
        occurrences = []
        for o in list_of_occurrences:
            for pair in SE.occurrences(o, line):
                occurrences.append(pair)
        for o in occurrences:
            self.text_widget.tag_add(tag, '{}.{}'.format(index, o[0]),
                                     '{}.{}'.format(index, o[1]))

    def highlight_re(self, tag, regexp):
        """Highlights all regular expressions matching regexp"""
        index = self.text_widget.index('insert').split('.')[0]
        line = self.line_text(index)
        self.text_widget.tag_remove(tag, '{}.{}'.format(index, 0),
                                    '{}.{}'.format(index, self.last_column(index)))
        occurrences = SE.occurrences_re(regexp, line)
        for o in occurrences:
            self.text_widget.tag_add(tag, '{}.{}'.format(index, o[0]),
                                     '{}.{}'.format(index, o[1]))

    def highlight(self, tag, start='1.0', end='end-1c'):
        self.text_widget.tag_add(tag, start, end)

    def unhighlight(self, tag, start='1.0', end='end-1c'):
        self.text_widget.tag_remove(tag, start, end)

    def set_new_language(self, new_language):
        self.remove_tags()
        self.language = new_language
        self.start()


if __name__ == '__main__':
    root = Tk()
    text_wid = Text(root)
    text_wid.pack(expand=1, fill='both')
    he = HE(text_wid, PythonLanguage())
    root.mainloop()
