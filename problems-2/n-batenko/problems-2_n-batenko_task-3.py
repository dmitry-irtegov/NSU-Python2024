from os import listdir, stat
from os.path import isfile, join

def __list_files(path : str):
    files = listdir(path)

    files_with_size = [(file, stat(join(path, file)).st_size) for file in files if isfile(join(path, file))]
    files_with_size = sorted(files_with_size, key=lambda x: (x[1], x[0]))

    return files_with_size

def __list_files_printer(list):
    

def list_files():
    input = input("Write path: ")
    result = __list_files(input)


print(list_files("/home/nikita/Languages/Python/test"))