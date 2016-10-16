#!/usr/bin/env bash

# Removes all .pyc and .pyo files, and __pycache__ directories.
# SOURCE: http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project

# Make this script executable first by doing: chmod +x clean.sh
# Run this file on the terminal with the following command: ./clean.sh 

find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete