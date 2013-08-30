#! /usr/bin/python -O

'''
Prints the directory structure in ASCII form.
'''

import os


INDENT = '  '

if __name__ == '__main__':

    for curRelPath, subdirs, files in os.walk('.'):

        (pathToFolder, folder) = os.path.split(curRelPath)
        parentDirs = pathToFolder.split(os.sep)
        numParentDirs = len(parentDirs)

        # If we are currently visiting the root of this traversal,
        # don't bother printing the folder name.  Otherwise, print the
        # folder name.
        if (numParentDirs == 1) and (parentDirs[0] == ''):
            fileLevel = 0;
        else:
            fileLevel = numParentDirs
            print INDENT * (numParentDirs - 1) + folder

        for curFile in files:
            print INDENT * fileLevel + curFile
