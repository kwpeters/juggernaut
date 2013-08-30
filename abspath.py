import sys
import os.path
import getopt

if __name__ == '__main__':

    (options, arguments) = getopt.getopt(sys.argv[1:], '')

    for argument in arguments:
        print os.path.abspath(argument)
