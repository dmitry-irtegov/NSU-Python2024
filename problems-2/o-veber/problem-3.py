from sys import argv
from os import listdir, stat
from os.path import isfile, join

directory_path = argv[1]
elements_in_dir = listdir(directory_path)
file_dict = {}
for element in elements_in_dir:
    element_absolute_path = join(directory_path, element)
    if isfile(element_absolute_path):
        file_dict[element] = stat(path=element_absolute_path).st_size
for file in sorted(file_dict.items(), key=lambda x: x[1], reverse=True):
    print(f'File with name=\"{file[0]}\" and size={file[1]}')
