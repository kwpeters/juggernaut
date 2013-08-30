#! /usr/bin/python -O

import os
import os.path
import platform
import editor

if __name__ == '__main__':
    homeDir = os.getenv('CLOUDHOME')

    machineName = platform.node()

    # The folder where notes files are kept.
    viewsFile = os.path.join(homeDir,
                             'data',
                             'programming',
                             'clearcase',
                             'clearcase_views_' + machineName + '.xml')

    # Invoke Emacs for this file.
    #executable = 'gnuclientw.exe'
    #os.system('%s "%s"' % (executable, viewsFile))
    editor.Open(viewsFile, False)
