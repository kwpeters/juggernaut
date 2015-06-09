#!/usr/bin/env python

import sys
import copybuf


if __name__ == '__main__':
    data = sys.stdin.readlines()
    data = ''.join(data)
    copybuf.AddToCopyBuf(data)
