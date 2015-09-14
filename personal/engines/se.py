"""
Author: Nelson Brochado
Creation: 6.02.2015
Last update: 12.02.2015

This module contains a class SE, which represents a Search Engine.
All methods in SE are static, and therefore can be accessed through the following syntax:
                            SE.method(args)
I put all functions in a class because I am a fan of the object oriented-paradigm.
The pair of indices returned is composed of: [starting_index, index_after_last_char]
For example, if the indices for the word 'are' in the string 'How are you"
would be: [4, 7] (7 is the index past the last letter)
Keep in mind indices start from 0.

Names conventions (of "SE"):
Methods that finish with "_re" were created specifically to search regular expressions.

All methods that start with "next_" have an optional parameter called "start",
which represents the index from where to start the search.

All methods that start with "full_" will return just indices of entire words (and not sub strings).
Note that these functions consider "you?" different from "you"!

More generic powerful functions are found at the end. Rawer simple functions are found at the beginning.

TODO:
 - performance of the algorithms has not been optimized...
 - I might not need both the functions that starts from a certain index
 and the function that simply returns everything.
 For example, maybe I just need "next_occurrences_re" instead of "occurrences_re",
 since the first can also do everything that the second does.
"""

import re


class SE(object):

    """Search Engine for my Editor,
    but it can also be used for other projects,
    since methods were thought to be as flexible as possible

    PARAMETERS:
    :param substring: "substring" to search in "string"
    :param string: the "string" where to search the "substring"
    :param sensitive: if True, does not ignore the case: "WORD" is different from "word",
    else it's ignored: "WORD" is considered equals to "word".
    :param overlapping: if True, possible sub strings are also searched, and not just entire words.
    :param pattern: regular expression to search in "string"
    :param word: entire word to search in "string".
    This is the same thing as passing to "pattern" or "substring", when "overlapping" is False.
    :param regexp: if True, it will use functions that end with "_re

    Note that functions that end with "_re" ignore what is case sensitive.
    """

    def __init__(self, *args, **kwargs):
        """Useless to create objects of this type,
        since all methods are static.
        """
        pass

    @staticmethod
    def occurrences(substring, string, sensitive=True):
        """Finds all overlapping occurrences of substring in string"""
        pos = -1
        o = []
        if not sensitive:
            substring = substring.lower()
            string = string.lower()
        while True:
            pos = string.find(substring, pos + 1)
            if pos == -1:
                return o
            else:
                o.append([pos, pos + len(substring)])

    @staticmethod
    def occurrences_re(pattern, string):
        """Uses "finditer" function of the "re" module to search for
        the starting and ending index of a (regular expression) pattern in a string."""
        exp = re.compile(pattern)
        o = []
        for i in exp.finditer(string):
            o.append([i.start(), i.end()])
        return o

    @staticmethod
    def full_words(word, string, sensitive=True):
        """Words are everything that is not a space and is not empty."""
        temp_word = ''
        o = []
        start = 0
        if not sensitive:
            word = word.lower()
            string = string.lower()
        for i, char in enumerate(string):
            if char != ' ':
                temp_word += char
                if i == 0:
                    start = 0
                else:
                    if string[i - 1] == ' ':
                        start = i
                if i == len(string) - 1:
                    if temp_word == word:
                        o.append([start, start + len(word)])
            else:
                if temp_word == word:
                    o.append([start, start + len(word)])
                temp_word = ''
        return o

    @staticmethod
    def next_word(word, string, start=0, sensitive=True):
        """Finds the first whole word starting from start, if any.
        If not whole word is found, [] is returned."""
        if start in range(0, len(string)):
            ls = SE.full_words(word, string[start:], sensitive)
            if ls:
                return [ls[0][0] + start, ls[0][1] + start]
        return []

    @staticmethod
    def next_occurrence(substring, string, start=0, sensitive=True):
        """Finds the next (possibly overlapping) occurrence of substring in string."""
        if start in range(0, len(string)):
            ls = SE.occurrences(substring, string[start:], sensitive)
            if ls:
                return [ls[0][0] + start, ls[0][1] + start]
        return []

    @staticmethod
    def next_occurrence_re(pattern, string, start=0):
        """Finds the next occurrence of pattern in string.
        Searches also for regular expressions."""
        exp = re.compile(pattern)
        for i in exp.finditer(string):
            if i.start() >= start:
                return [i.start(), i.end()]
        return []

    @staticmethod
    def next_occurrences(substring, string, start=0, sensitive=True):
        if start in range(0, len(string)):
            next_occurrences = SE.occurrences(substring, string[start:], sensitive)
            for o in next_occurrences:
                o[0] += start
                o[1] += start
            return next_occurrences
        else:
            return []

    @staticmethod
    def next_words(substring, string, start=0, sensitive=True):
        if start in range(0, len(string)):
            words = SE.full_words(substring, string[start:], sensitive)
            for o in words:
                o[0] += start
                o[1] += start
            return words
        else:
            return []

    @staticmethod
    def next_occurrences_re(pattern, string, start=0):
        if start in range(0, len(string)):
            occurrences_re = SE.occurrences_re(pattern, string[start:])
            for o in occurrences_re:
                o[0] += start
                o[1] += start
            return occurrences_re
        else:
            return []

    # The following 3 methods should be used,
    # if you want functions with all possible options of searching
    @staticmethod
    def count(pattern, string, overlapping=True, sensitive=True, regexp=False):
        """Returns the length of the returned value of the call to findall"""
        return len(SE.findall(pattern, string, overlapping, sensitive, regexp))

    @staticmethod
    def findall(pattern, string, overlapping=True, sensitive=True, regexp=False):
        """if regexp is set to True, then overlapping and sensitive are ignored"""
        if regexp:
            return SE.occurrences_re(pattern, string)
        if overlapping:
            return SE.occurrences(pattern, string, sensitive)
        else:
            return SE.full_words(pattern, string, sensitive)

    @staticmethod
    def find(pattern, string, start=0, overlapping=True, sensitive=True, regexp=False):
        """Returns the first occurrence after start (inclusive).
        If regexp is True, then sensitive and overlapping are ignored.
        """
        if regexp:
            return SE.next_occurrence_re(pattern, string, start)
        if not overlapping:  # whole words
            return SE.next_word(pattern, string, start, sensitive)
        else:
            return SE.next_occurrence(pattern, string, start, sensitive)


pat = '[0-9]'
pat2 = r'\b\d+\b'  # find numbers
sub = 'are'
text = "How old are you ? I am22, you are 20. Aren't you? Are you ok?"

if __name__ == '__main__':
    # Change sensitive to see the difference
    oc = SE.occurrences(sub, text, sensitive=False)
    print(oc)

    oc_re = SE.occurrences_re(sub, text)
    print(oc_re)
    oc_re2 = SE.occurrences_re(sub, text)
    print(oc_re2)

    f_words = SE.full_words('you', text, False)
    print(f_words)

    # Search from index 9 (ignoring the case)
    n_word = SE.next_word(sub, text, 9, sensitive=True)
    print(n_word)

    n_o = SE.next_occurrence(sub, text, 32, sensitive=False)
    print(n_o)
    n_o2 = SE.next_occurrence(sub, text, 40, sensitive=True)
    print(n_o2)

    # Searches for numbers. The 12 in abc12def is not considered a number!
    f_all = SE.findall(pat2, text, overlapping=True, sensitive=True, regexp=True)
    print(f_all)
    f_all2 = SE.findall(pat2, text, overlapping=True, sensitive=True, regexp=False)
    print(f_all2)
