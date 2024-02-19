#!/usr/bin/env python3
import os
import os.path

if __name__ == '__main__':
    filenames = list(filter(os.path.isfile, os.listdir(path='.')))
    sizes = list(map(lambda filename: os.stat(os.path.join('.', filename)).st_size, filenames))

    for filename, size in sorted(zip(filenames, sizes), key=lambda x: (-x[1], x[0])):
        print(f'{filename}: {size} B')
