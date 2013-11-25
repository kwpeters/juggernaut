import os
import platform

OPEN_IN_EXISTING_EDITOR_EXECUTABLE = 'my_emacsclient -n'
OPEN_IN_NEW_EDITOR_EXECUTABLE      = 'my_emacs'

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
