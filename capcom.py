#!/usr/bin/env python -O
import editor
import todo
import captlog
import notes

if __name__ == '__main__':
    # Append to the captlog file if needed.
    captlogLauncher = captlog.CaptLogLauncher()
    captlogLauncher.AppendToCaptlogIfNeeded()

    # Launch the editor.
    todoFile = todo.TodoLauncher().GetFilePath();
    captlogFile = captlogLauncher.GetFilePath();
    notesFolder = notes.NotesLauncher().GetFolder()

    editor.Open(' '.join([notesFolder, captlogFile, todoFile]), False)

