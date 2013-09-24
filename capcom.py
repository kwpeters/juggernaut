#! /usr/bin/python -O
import editor
import todo
import captlog
import notes

if __name__ == '__main__':

    todoFile = todo.TodoLauncher().GetFilePath();
    captlogFile = captlog.CaptLogLauncher().GetFilePath();
    notesFolder = notes.NotesLauncher().GetFolder()

    editor.Open(' '.join([todoFile, captlogFile, notesFolder]), False)

