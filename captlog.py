#! /usr/bin/python -O

'''
This program creates a daily log file when run.  The current time is
appended to the end of the file.
'''
import sys
import datetime
import os
import os.path
import editor
import getopt


def GetDailyDelimiterLine():
    r'''Returns the delimiter line that is used between days.'''
    now = datetime.datetime.now()
    dateStr = now.strftime('%Y-%m-%d (%A)')
    delim = '* ' + dateStr
    return delim


def NeedToAppendDailyTemplate(logFile):
    r'''Determines whether the specified log file needs to have the
    daily template appended to it.'''

    delimLine = GetDailyDelimiterLine()

    inputFile = open(logFile, 'r')
    lines = inputFile.readlines()
    lines = [line.strip() for line in lines]

    if delimLine in lines:
        print "File already has an entry for today's date."
        return False
    else:
        print 'Did not find "%s" in the file.' % delimLine
        return True


def AppendDailyTemplate(logFile):
    r'''This function appends a daily template to the specified log
    file.'''

    output = open(logFile, 'a')
    output.write('%s\n' % GetDailyDelimiterLine())
    output.write('** Time\n')

    timeTemplate = r'''    |---+-----+--------------------------------------------------|
    |   |     | Mobility Foundation - Aguila      (SAP 2521.1)   |
    |---+-----+--------------------------------------------------|
    |   |     | AOP 11x (v22)                     (SAP 2520.1.1) |
    |---+-----+--------------------------------------------------|
    |   |     | Training                              (SAP 1440) |
    |---+-----+--------------------------------------------------|
    |   |     | Misc Meeting                          (SAP 1210) |
    |---+-----+--------------------------------------------------|
    |   |     | Misc                                  (SAP 1110) |
    |---+-----+--------------------------------------------------|
    |   |     | Floater                                (SAP 360) |
    |---+-----+--------------------------------------------------|
    |   |     | Vacation                               (SAP 200) |
    |---+-----+--------------------------------------------------|
    |   |     | Sick/Personal                          (SAP 230) |
    |---+-----+--------------------------------------------------|
    | # |     | TOTAL                                            |
    | ^ | tot |                                                  |
    |---+-----+--------------------------------------------------|
   #+TBLFM: $tot=vsum(@1..@-1)
'''
    output.write(timeTemplate)

    output.write('** Journal\n')
    output.close()


def GetUsage():
    r'''This function returns a string with usage information for this
    script.'''

    return r'''
Creates an entry into my captain's log file and opens it.

Usage:
    captlog.py [-r]

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


    cloudHome = os.getenv('DROPBOXHOME')
    logFile = os.path.abspath(os.path.join(cloudHome, 'data', 'captlog.org'))

    if NeedToAppendDailyTemplate(logFile):
        AppendDailyTemplate(logFile)

    editor.Open(logFile, reuseEditor)
