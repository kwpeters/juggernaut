#! python -O
'''
This program edits my personal cheat sheet.
'''

import os
import os.path
import editor

if __name__ == '__main__':

    homeDir = os.getenv('CLOUDHOME')
    cheatsheetFile = os.path.abspath(os.path.join(homeDir, 'data', 'cheat_sheet', 'index.html'))

    editor.Open(cheatsheetFile, False);
