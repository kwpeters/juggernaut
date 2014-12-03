#! python

import sys
import copybuf

if __name__ == '__main__':
    args = sys.argv[1:]
    args = ' '.join(args) + '\n'
    copybuf.AddToCopyBuf(args)
