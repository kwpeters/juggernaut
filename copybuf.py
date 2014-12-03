import os
import os.path
import win32clipboard


def SetClipboardText(str):
    win32clipboard.OpenClipboard(0)
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(str)
    win32clipboard.CloseClipboard()


def GetCopyBufFileName():
    # If there is no home directory on this PC, just return None.
    if not os.environ.has_key('home'):
	return None

    file = os.path.join(os.environ['home'], 'copybuf.txt')
    return file


def OpenCopyBufInEmacs():
    filename = GetCopyBufFileName()

    if filename:
	# Invoke Emacs and load the copybuf.txt file.
	# F: uniconify if necessary
	# f: bring to front
	executable = 'gnuclientw.exe -Ff'
	os.system('%s "%s"' % (executable, filename))


def AddToCopyBuf(text):
    # Put the text on the Windows clipboard.
    SetClipboardText(text)

    # Try to put the text in the copybuf file.
    filename = GetCopyBufFileName()
    if filename:
        output = open(filename, 'a')
        output.write(text)
        output.close()


if __name__ == '__main__':
    OpenCopyBufInEmacs()
