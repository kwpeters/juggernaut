#!/usr/bin/env python
import editor
import todo
import captlog
import clippalette
import notes

if __name__ == '__main__':
    # Append to the captlog file if needed.
    captlogLauncher = captlog.CaptLogLauncher()
    captlogLauncher.AppendToCaptlogIfNeeded()

    # Launch the editor.
    todoFile = todo.TodoLauncher().GetFilePath();
    clipPaletteFile = clippalette.ClipPalette().GetFilePath();
    captlogFile = captlogLauncher.GetFilePath();
    notesFolder = notes.NotesLauncher().GetFolder()

    # Put most frequently used files last so they will be on the top
    # of the buffer stack.
    editor.Open(' '.join([clipPaletteFile, notesFolder, captlogFile, todoFile]), False)
