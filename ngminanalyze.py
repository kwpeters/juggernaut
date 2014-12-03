#!/usr/bin/env python
import os
import os.path

def ProcessJsFile(jsFile):
    print 'Processing %s...' % (jsFile)
    outputFile = os.path.join(r'c:\tmp', 'ngmin_output.js')

    cmd = 'ngmin --dynamic "%s" "%s"' % (jsFile, outputFile)
    os.system(cmd)
    
    cmd = 'winmergeu "%s" "%s"' % (jsFile, outputFile)
    os.system(cmd)


if __name__ == '__main__':
    jsFiles = []

    for (root, dirs, files) in os.walk('.'):
        for curFile in files:

            baseName, extName = os.path.splitext(curFile)
            isSpecFile = baseName.endswith('.spec')

            if (extName == '.js') and (not isSpecFile):
                curPath = os.path.join(root, curFile)
                jsFiles.append(curPath)

for curJsFile in jsFiles:
    ProcessJsFile(curJsFile)
