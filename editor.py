import os
import platform

OPEN_IN_EXISTING_EDITOR_EXECUTABLE = 'emacsclient -n'
OPEN_IN_NEW_EDITOR_EXECUTABLE      = '/usr/local/Cellar/emacs/24.4/Emacs.app/Contents/MacOS/Emacs'

def Open(fileToOpen, openInExistingEditor=True):

    if platform.system() == 'Windows':
        # Running on Windows.

        if openInExistingEditor:
            #executable = 'gnuclientw.exe'
            executable = 'emacsclient.exe'
        else:
            executable = 'runemacs'

    else:
        # Running on Mac
        if openInExistingEditor:
            executable = OPEN_IN_EXISTING_EDITOR_EXECUTABLE
        else:
            executable = OPEN_IN_NEW_EDITOR_EXECUTABLE

    cmd = '%s %s &' % (executable, fileToOpen)
    os.system(cmd)
