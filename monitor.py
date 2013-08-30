#! /usr/bin/python -O
'''
This program monitors a set of folders and executes a command when anything changes.
'''

import sys
import getopt
import os
import os.path
import time
import re
import utility

def GetUsage():
    return r'''
Monitors files and executes a command when they are modified.

Usage:
    monitor.py --help
    monitor.py [--dir <dir>] [--include <regex]
               [--exclude <regex>] [--cmd <command>]
'''

def GenerateModTimeMap(dirs, includeRegexes, excludeRegexes):
    fileModTimeDict = {}

    for curDir in dirs:
        for (root, dirs, files) in os.walk(curDir):
            for curFile in files:

                curFilePath = os.path.join(root, curFile)
                curAbsPath = os.path.abspath(curFilePath)

                # Only index the file if it is being included and is
                # not being excluded.
                if (utility.MatchesAny(curFilePath, includeRegexes) and
                    not utility.MatchesAny(curFilePath, excludeRegexes)):
                    modTime = os.path.getmtime(curFilePath)
                    fileModTimeDict[curAbsPath] = modTime

    return fileModTimeDict


def ExecuteCommand(cmd, modifiedFile):
    if cmd:
        # Execute the command on the modified file.
        quotedFile = '"' + modifiedFile + '"'
        fullCommand = cmd + ' ' + quotedFile
        print fullCommand
        os.system(fullCommand)
    else:
        # No command specified.  Just log a message that the file was changed.
        print 'Change detected:  %s' % modifiedFile


if __name__ == '__main__':

    dirs = []
    includeRegexes = []
    excludeRegexes = []
    command = None

    (options, args) = getopt.getopt(
        sys.argv[1:],
        '',
        ['help', 'dir=', 'include=', 'exclude=', 'cmd=']
        )
    for (option, value) in options:

        if option == '--help':
            print GetUsage()
            sys.exit(0)

        elif option == '--dir':
            dirs.append(value)

        elif option == '--include':
            includeRegexes.append(value)

        elif option == '--exclude':
            excludeRegexes.append(value)

        elif option == '--cmd':
            command = value

        else:
            print 'Unknown command line option: %s.' % option
            print GetUsage()
            sys.exit(1)

    # If the user did not specify certain parameters, assume defaults.
    if len(dirs) == 0:
        dirs = ['.']

    if len(includeRegexes) == 0:
        includeRegexes = ['.*']

    # Print information.
    print 'Directories:  %s' % dirs
    print 'Include:      %s' % includeRegexes
    print 'Exclude:      %s' % excludeRegexes
    print 'Command:      %s' % command

    includeRegexes = [re.compile(curStr, re.IGNORECASE) for curStr in includeRegexes]
    excludeRegexes = [re.compile(curStr, re.IGNORECASE) for curStr in excludeRegexes]

    modTimeMap = GenerateModTimeMap(['.'], includeRegexes, excludeRegexes)
    print '%d files being watched.' % len(modTimeMap)

    while True:
        for curAbsPath in modTimeMap:
            newModTime = os.path.getmtime(curAbsPath)
            if newModTime > modTimeMap[curAbsPath]:
                ExecuteCommand(command, curAbsPath)
                modTimeMap[curAbsPath] = newModTime

        time.sleep(3)

