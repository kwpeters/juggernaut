#!/usr/bin/env python
import os.path
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
    notesFolder = notes.NotesLauncher().GetFolder();

    homeDir = os.getenv('HOME');
    lemansCommonServicesFilePath = os.path.abspath(os.path.join(homeDir, "OneDrive - Rockwell Automation, Inc", "home", "rok_data", "projects", "lemans", "common services", "common_services.org"));
    lemansCommonServicesFilePath = '"' + lemansCommonServicesFilePath + '"';


    # Put most frequently used files last so they will be on the top
    # of the buffer stack.
    editor.Open(' '.join([clipPaletteFile, notesFolder, lemansCommonServicesFilePath, captlogFile, todoFile]), False)
