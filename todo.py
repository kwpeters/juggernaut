#! /usr/bin/python -O
import sys
import os
import os.path
import getopt
import editor


def GetUsage():
    r'''This function returns a string with usage information for this
    script.'''

    return r'''
Opens my todo file.

Usage:
    todo.py [-r]

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

    cloudHome = os.getenv('DROPBOXHOME')
    todoFile = os.path.abspath(os.path.join(cloudHome, 'data', 'todo.org'))

    editor.Open(todoFile, reuseEditor)
