"""
Author: Nelson Brochado
Creation: End of 2014
Last update: 30.01.2015

Description:
This module contains the base class Language,
which represents a (programming) language.
There are also other derived classes, such as PythonLanguage or CppLanguage

DEPENDENCIES:
- modules "python", "cpp", "ijvm"

BE CAREFUL:
Due to importing problems, to run this module,
you should remove . from the imports below that contain it.

Note that you should then insert them at the end,
because other modules, such as HE, need that imports done like that.
"""

from collections import OrderedDict
import pprint

from .python import builtins_
from .python import keywords as py_kw
from .cpp import keywords as cpp_kw
from .ijvm import keywords as ijvm_kw


class Language:

    """Base class for a programming language"""
    
    DEFAULT_FONT = ('monaco', 12, 'normal')
    
    # 3 ways to search syntax parts
    SEARCH = ('word', 'occurrence', 'regexp')

    def __init__(self, *args, **options):
        self.name = options.pop('name', 'language')
        self.normal = {'value': '', 'fg': '#000', 'bg': '#fff', 'font': Language.DEFAULT_FONT,
                       'search': 'word', 'tag': self.name + '_' + 'normal'}

        # The value of the 'search' key defines the way of searching the value
        # of the key 'value'
        self.syntax = OrderedDict([
            ('keywords', {'value': [], 'fg': 'orange', 'bg': '#fff', 'font': Language.DEFAULT_FONT,
                          'search': self.SEARCH[0], 'tag': self.name + '_' + 'keywords'}),
            (
                'operators', {'value': ['+', '-', '*', '/', '%'], 'fg': '#14b', 'bg': '#fff', 'font': Language.DEFAULT_FONT,
                              'search': self.SEARCH[1], 'tag': self.name + '_' + 'operators'}),
            ('builtins', {'value': [], 'fg': '#00f', 'bg': '#fff', 'font': Language.DEFAULT_FONT,
                          'search': self.SEARCH[1], 'tag': self.name + '_' + 'builtins'}),
            ('numbers', {'value': r'\b\d+\b', 'fg': '#f05', 'bg': '#fff', 'font': Language.DEFAULT_FONT,
                         'search': self.SEARCH[2], 'tag': self.name + '_' + 'numbers'}),
            ('strings', {'value': r'("([^"]*)")|(\'([^"]*)\')', 'fg': '#139E5F', 'bg': '#fff',
                         'font': Language.DEFAULT_FONT, 'search': self.SEARCH[2], 'tag': self.name + '_' + 'strings'}),
            ('brackets', {'value': ['[', ']', '{', '}', '(', ')'], 'fg': '#83B3F0', 'bg': '#fff',
                          'font': Language.DEFAULT_FONT, 'search': self.SEARCH[1], 'tag': self.name + '_' + 'brackets'})
        ])

    def show(self):
        pprint.pprint(self.syntax)


class PythonLanguage(Language):

    """Python language class"""

    def __init__(self, *args, **options):
        Language.__init__(self, *args, **options)
        self.name = 'python'
        self.syntax['keywords']['value'] = py_kw.KEYWORDS
        self.syntax['builtins']['value'] = builtins_.BUILTINS


class CppLanguage(Language):

    """C++ language class"""

    def __init__(self, *args, **options):
        Language.__init__(self, *args, **options)
        self.name = 'cpp'
        self.syntax['keywords']['value'] = cpp_kw.KEYWORDS
        self.syntax['keywords']['search'] = self.SEARCH[1]
        self.syntax['numbers']['value'] = r'\d+'


class IJVMLanguage(Language):

    """IJVM language class"""

    def __init__(self, *args, **options):
        Language.__init__(self, *args, **options)
        self.name = 'ijvm'
        self.syntax['keywords']['value'] = ijvm_kw.KEYWORDS


if __name__ == '__main__':
    lang = Language()
    python = PythonLanguage()
    python.show()
    cpp = CppLanguage()
    cpp.show()
    ijvm = IJVMLanguage()
    ijvm.show()
