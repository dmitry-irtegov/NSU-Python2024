import argparse
import sys


class Tr:
    def __init__(self, replace_from, replace_to, delete_chars=None):
        self._file_path = None
        if len(replace_from) != len(replace_to):
            raise ValueError('Characters to replace and replacement characters must be the same length')
        if len(replace_from) != len(set(replace_from)):
            raise ValueError('Replacement characters must not be repeated')
        self._replace_from = replace_from
        self._replace_to = replace_to
        self._delete_chars = delete_chars

    def _read_file(self):
        self._file_path = input("Enter the path to the file: ")
        try:
            with open(self._file_path, "r") as file:
                return file.readlines()
        except OSError as e:
            e.strerror = f'An error occurred while reading file {self._file_path}: {e.strerror}'
            raise e

    def _write_file(self, res):
        while True:
            mod = input("Modify this file or create a new one? this/new ")
            try:
                if mod == "this":
                    file = open(self._file_path, 'w')
                    break
                elif mod == "new":
                    file = open(f'tr_{self._file_path}', 'w')
                    break
            except OSError as e:
                e.strerror = f'An error occurred while writing file {self._file_path}: {e.strerror}'
                raise e
        with file:
            file.writelines(res)

    def translate_line(self, line):
        res = ''
        for c in line:
            if self._delete_chars and c in self._delete_chars:
                continue
            if c in self._replace_from:
                res += self._replace_to[self._replace_from.index(c)]
            else:
                res += c
        return res

    def translate_file(self):
        lines = self._read_file()
        res = [''] * len(lines)
        for i, line in enumerate(lines):
            res[i] = self.translate_line(line)
        self._write_file(res)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("replace_from", help="Characters to replace")
    parser.add_argument("replace_to", help="Replacement characters")
    parser.add_argument("-d", "--delete", help="Characters to delete")
    args = parser.parse_args()

    try:
        tr = Tr(args.replace_from, args.replace_to, args.delete)
    except Exception as e:
        sys.stderr.write(f'Problem with arguments: {repr(e)}')
        exit(1)
    try:
        tr.translate_file()
    except OSError as e:
        sys.stderr.write(e.strerror)
        exit(1)
    except KeyboardInterrupt:
        print("The process was interrupted")
    except Exception as e:
        sys.stderr.write(f'An error occurred during translation: {e}')


if __name__ == "__main__":
    main()
