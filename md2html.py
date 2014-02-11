#!/usr/bin/env python -O

import sys
import getopt
import os
import os.path


def GetUsage():
    return r'''
Compiles a markdown file into HTML.

Usage:
    md2html.py --help
    md2html.py [--cssFile <path-to-css-file>] md_file_1 md_file_2

    where:

    --help

        Displays this help text.

    --cssFile <path-to-css-file>

        Specifies the path to a CSS file that will have a
        corresponding <link> element appended to the resulting HTML
        file.  This switch may be used multiple times to include
        multiple CSS files.
'''


def AppendCss(filename, cssFiles):

    newLines = ['<link rel="stylesheet" href="%s">' % cssFile for cssFile in cssFiles]

    outputObj = open(filename, 'a')
    outputObj.writelines(newLines)
    outputObj.close()


if __name__ == '__main__':

    cssFiles = []

    (options, args) = getopt.getopt(
        sys.argv[1:],
        '',
        ['help',
         'cssFile='])

    for (option, value) in options:

        if option == '--help':
            print GetUsage()
            sys.exit(0)

        elif option == '--cssFile':
            if os.path.isfile(value):
                cssFiles.append(value)
            else:
                print '%s is not a file.' % value
                sys.exit(1)

        else:
            print 'Unknown command line option: %s.' % option
            print GetUsage()
            sys.exit(1)


    for curMdFile in args:
        if os.path.isfile(curMdFile):
            basename = os.path.splitext(os.path.basename(curMdFile))[0]
            outputFile = basename + '.html'
            cmd = 'marked --gfm --tables -i %s -o %s' % (curMdFile, outputFile)
            print cmd
            os.system(cmd)

            if os.path.isfile(outputFile):
                AppendCss(outputFile, cssFiles)

        else:
            print 'File does not exist:  %s' % curMdFile
