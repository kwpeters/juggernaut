#!/usr/bin/env python

'''
This program opens a clipPalette.org file.
'''
import sys
import datetime
import os
import os.path
import editor
import getopt

class ClipPalette(object):


    def __init__(self):
        pass


    def GetFilePath(self):
        cloudHome = os.getenv('DROPBOXHOME')
        absPath = os.path.abspath(os.path.join(cloudHome, 'data', 'clippalette.org'))
        return absPath


    def Launch(self, reuseEditor):
        absPath = self.GetFilePath()
        editor.Open(absPath, reuseEditor)


def GetUsage():
    r'''This function returns a string with usage information for this
    script.'''

    return r'''
Opens the clippalette.org file.

Usage:
    clippalette.py [-r]

    Where:

        -r  To reuse an already open editor window

'''


if __name__ == '__main__':

    reuseEditor = False;

    (options, args) = getopt.getopt(sys.argv[1:], 'r', ['help'])
    for (option, value) in options:
        if option == '--help':
            print GetUsage()
            sys.exit(0)
        elif option == '-r':
            reuseEditor = True

    launcher = ClipPalette()
    launcher.Launch(reuseEditor)
