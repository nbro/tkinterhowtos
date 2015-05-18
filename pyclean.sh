#!/usr/bin/env bash

# pyclean removes all .pyc and .pyo files, and __pycache__ directories.
# SOURCE: http://stackoverflow.com/questions/785519/how-do-i-remove-all-pyc-files-from-a-project

# Run this file on the terminal with the following command: ./pyclean.sh 
# Make this script executable first by doing: chmod +x pyclean.sh

pyclean() {
    find . -type f -name "*.py[co]" -delete && find . -type d -name "__pycache__" -delete 
}

pyclean