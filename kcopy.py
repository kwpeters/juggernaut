#!/usr/bin/env python

import sys
import getopt
import os
import os.path
import re
import utility
import shutil


SEP = '--------------------------------------------------------------------------------'


def GetUsage():
    return r'''
Copies files.

Usage:
    kcopy.py --help
    kcopy.py --dryrun [--ignore <regex>] src
    kcopy.py [--ignore <regex>] src dest

    where:

    --ignore <regex>
        All files matching the regular expression will be skipped.
        This switch may be used multiple times to ignore multiple
        patterns

    src
        The source of files to copy

    dest
        The destination
'''

def GetSourceFiles(srcFolder, ignorePatterns):

    filesToCopy = []
    filesToIgnore = []

    for dirPath, dirNames, fileNames in os.walk(srcFolder):

        for curFileName in fileNames:
            curPath = os.path.join(dirPath, curFileName)
            assert curPath.startswith(srcFolder)

            # Make a path relative to the srcFolder.
            curRelPath = curPath[len(srcFolder) + 1:]

            if utility.MatchesAny(curPath, ignorePatterns):
                filesToIgnore.append(curRelPath)
            else:
                filesToCopy.append(curRelPath)

    return (filesToCopy, filesToIgnore)


def PerformCopy(srcFolder, destFolder, filesToCopy):
    for curFile in filesToCopy:
        srcPath = os.path.join(srcFolder, curFile)
        destPath = os.path.join(destFolder, curFile)

        print
        print 'Copying...'
        print '    ' + srcPath
        print '    ' + destPath
        #print '%s ==> %s' % (srcPath, destPath)

        utility.CreateDirForFile(destPath)
        shutil.copy2(srcPath, destPath)


if __name__ == '__main__':

    srcFolder = None
    destFolder = None
    ignorePatterns = []
    dryRun = False

    (options, args) = getopt.getopt(
        sys.argv[1:],
        '',
        ['help',
         'ignore=',
         'dryrun'])

    for (option, value) in options:

        if option == '--help':
            print GetUsage()
            sys.exit(0)

        elif option == '--ignore':
            ignorePatterns.append(value)

        elif option == '--dryrun':
            dryRun = True

        else:
            print 'Unknown command line option: %s.' % option
            print GetUsage()
            sys.exit(1)

    # Check that the correct number of arguments were provided.
    if (dryRun):
        # When doing a dry run, we need one argument (src).
        if len(args) < 1:
            print 'No src argument specified.'
            sys.exit(1)
    else:
        # When not doing a dry run, we need two arguments (src, dest).
        if len(args) < 2:
            print 'You need to specify both a src and dest directory!'
            sys.exit(1)

    # We will always have a src argument.
    srcFolder = args[0] if len(args) >= 1 else None

    # We may have a dest argument.
    if len(args) >= 2:
        destFolder = args[1]

    # Validate the src folder.
    if not os.path.isdir(srcFolder):
        print '%s is not a directory!' % srcFolder
        sys.exit(1)

    # Validate the dest folder.
    if destFolder and not os.path.isdir(destFolder):
        print '%s is not a directory!' % destFolder
        sys.exit(1)

    print SEP
    print 'source folder:       ' + srcFolder

    if destFolder:
        print 'destination folder:  ' + destFolder

    print 'dry run:             ' + str(dryRun)
    print 'ignore patterns:     ' + '  '.join(['"' + curPattern + '"' for curPattern in ignorePatterns])

    # Convert the ignore patterns into regular expression objects.
    ignorePatterns = [re.compile(curRegex, re.IGNORECASE) for curRegex in ignorePatterns]

    (filesToCopy, filesToIgnore) = GetSourceFiles(srcFolder, ignorePatterns)

    print SEP
    print 'Files to be copied (%d):' % len(filesToCopy)
    print '\n'.join(filesToCopy)

    print SEP
    print 'Ignored files (%d):' % len(filesToIgnore)
    print '\n'.join(filesToIgnore)

    # If we are just doing a dry run, stop now.
    if dryRun:
        sys.exit(0)

    print SEP
    PerformCopy(srcFolder, destFolder, filesToCopy)

