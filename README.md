# tkinterhowtos

[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)

## Introduction

This repository contains solutions to _simple_ "how to" problems in `tkinter`,
that is problems you would ask help about by asking questions that start with
"how to". An example of a question is _how to remove a row from a `Treeview`?_.

## Goal

The aim of this project is to decrease the time looking up in the documentation
and/or in websites like Stack Overflow for solutions to recurrent simple
"how to" problems (while developing a `tkinter` GUI). It does that by providing
concrete implementations of solutions (which you can simply copy and paste or, 
in general, easily adjust to your needs) and a logically structured repository.

## Structure

The folder `widgets` contains examples of solutions to "how to" problems related
only to specific widgets. For example, in `widgets/Text` we can find the file
[`style_parts_of_text.py`](widgets/Text/style_parts_of_text.py), which basically
contains an  example of a solution on how to style certain parts of text (or
simple words) in a `Text` widget.

Every file is intended to contain solutions to one single problem. Examples are
concise. Each module's doc-strings contains a list of the references used while
implementing the example.

## References

Many solutions to "how to" problems in this repository have been based on
solutions I found on websites such as Stack Overflow. So, even if I'm the author
of the concrete implementations in this repository, in many (or most) cases I'm 
not the originator of the ideas used to implement the solutions.
