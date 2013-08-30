#! /usr/bin/python -O
'''
This program opens my personal cheat sheet.
'''

import os
import os.path
import sys
import getopt
import editor


def GetUsage():
    r'''This function returns a string with usage information for this
    script.'''

    return r'''
Opens my cheat sheet file.

Usage:
    cheatsheet.py [-r]

    Where:

        -r  To reuse an already open editor window

'''


if __name__ == '__main__':

    reuseEditor = False

    (options, args) = getopt.getopt(sys.argv[1:], 'r', ['help'])
    for (option, value) in options:
        if option == '--help':
            print GetUsage()
            sys.exit(0)
        elif option == '-r':
            reuseEditor = True

    homeDir = os.getenv('CLOUDHOME')
    cheatsheetFile = os.path.abspath(os.path.join(homeDir, 'data', 'cheat_sheet', 'cheatsheet.txt'))

    editor.Open(cheatsheetFile, reuseEditor)
