"""
Testing the HE engine

Author: Nelson Brochado

DEPENDENCIES:
- submodule "lang"
- module "util"
- module "he"
"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText

from he import HE
from lang.language import *


class LanguageText(ScrolledText):
    """Scrolled text widget with a few more features,
    such as language highlighting for certain programming languages"""

    def __init__(self, parent, language, **options):
        ScrolledText.__init__(self, parent, **options)
        self.config(undo=True, tabs='0.4i')
        self.focus()
        # This is set to True, when the contents of self are store to the file
        # system.
        self.saved = False
        self.bind('<Command-a>', lambda e: self.tag_add('sel', 1.0, 'end'))
        self.language = language
        self.highlighter = HE(self, self.language)

    def text(self, start=1.0, end='end-1c'):
        """Returns the content of the ScrolledText object"""
        return self.get(start, end)

    def set_text(self, text):
        """Sets the string text of this object"""
        self.delete(1.0, 'end-1c')
        self.insert(1.0, text)

    def set_new_language(self, new_language):
        self.highlighter.set_new_language(new_language)


class Pad(Toplevel):
    """Simple note pad demonstration"""

    def __init__(self, master, size=(500, 400), pos=(260, 300)):
        Toplevel.__init__(self, master)
        self.text = LanguageText(self, CppLanguage())
        self.text.pack(expand=1, fill='both')
        self.current = Label(self, text='Language: ' + self.text.language.name, relief="groove")
        self.current.pack(side='right')
        self.get_lang_menu()

    def set_python_syntax(self):
        self.current.config(text='Language: Python')
        self.text.set_new_language(PythonLanguage())

    def set_cpp_syntax(self):
        self.current.config(text='Language: C++')
        self.text.set_new_language(CppLanguage())

    def get_lang_menu(self):
        menubar = Menu(self)
        languages = Menu(menubar, tearoff=0)
        languages.add_command(label='Python', command=self.set_python_syntax)
        languages.add_command(label='C++', command=self.set_cpp_syntax)
        menubar.add_cascade(label='Languages', menu=languages)
        self.config(menu=menubar)


def main():
    import util

    master = Tk()
    master.withdraw()

    pad = Pad(master)
    util.make_topmost(pad)
    pad.focus_force()

    master.mainloop()


if __name__ == "__main__":
    main()
