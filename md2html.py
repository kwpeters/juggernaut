#! /usr/bin/python -O

import sys
import getopt
import os
import os.path


def GetUsage():
    return r'''
Compiles a markdown file into HTML.

Usage:
    monitor.py --help
    monitor.py md_file_1 md_file_2
'''


if __name__ == '__main__':

    (options, args) = getopt.getopt(
        sys.argv[1:],
        '',
        ['help'])

    for (option, value) in options:

        if option == '--help':
            print GetUsage()
            sys.exit(0)

        else:
            print 'Unknown command line option: %s.' % option
            print GetUsage()
            sys.exit(1)


    for curMdFile in args:
        if os.path.isfile(curMdFile):
            basename = os.path.splitext(os.path.basename(curMdFile))[0]
            cmd = 'marked --gfm --tables -i %s -o %s.html' % (curMdFile, basename)
            print cmd
            os.system(cmd)

        else:
            print 'File does not exist:  %s' % curMdFile


