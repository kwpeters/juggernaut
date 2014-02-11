#!/usr/bin/env python -O

import sys
import os
import hashlib

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                files_with_hash = hashes.get(file_id, None)
                if files_with_hash:
                    files_with_hash.append(full_path)
                else:
                    hashes[file_id] = [full_path]

    for file_id, files in hashes.items():
        if len(files) > 1:
            print 'Duplicates found:'
            print '\n'.join(files)
            print

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print "Please pass the paths to check as parameters to the script"
