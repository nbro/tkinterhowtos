"""
Some utility functions for all the classes under "engines"

Author: Nelson Brochado
"""


def make_topmost(toplevel):
    toplevel.lift()
    toplevel.attributes("-topmost", 1)
    toplevel.attributes("-topmost", 0)
