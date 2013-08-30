import os
import platform

OPEN_IN_EXISTING_EDITOR_EXECUTABLE = 'my_emacsclient -n'
OPEN_IN_NEW_EDITOR_EXECUTABLE      = 'my_emacs'

def Open(fileToOpen, openInExistingEditor=True):

    if platform.system() == 'Windows':
        # Running on Windows.

        # When running in Windows, we don't care about the
        # openInExistingEditor flag right now.
        executable = 'gnuclientw.exe'

    else:
        # Running on Mac
        if openInExistingEditor:
            executable = OPEN_IN_EXISTING_EDITOR_EXECUTABLE
        else:
            executable = OPEN_IN_NEW_EDITOR_EXECUTABLE

    os.system('%s "%s" &' % (executable, fileToOpen))
