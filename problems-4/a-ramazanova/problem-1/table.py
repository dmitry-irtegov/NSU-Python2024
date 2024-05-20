import argparse
import sys


class InvalidInputTable(Exception):
    pass


class Table:
    def __init__(self, data):
        self._data = data
        self._validate_data()

    def get_data(self):
        return self._data

    def _validate_data(self):
        if not isinstance(self._data, list) or not all(isinstance(row, list) for row in self._data):
            raise TypeError("Table data must be a list of lists")
        if self._data:
            row_len = len(self._data[0])
            if any(len(row) != row_len for row in self._data):
                raise ValueError("All rows in the table must have the same length")

    def head(self, n):
        return Table(self._data[:n])

    def tail(self, n):
        return Table(self._data[-n:])

    def select_rows(self, indices):
        return Table([self._data[i] for i in indices if i < len(self._data)])

    def append_rows(self, other_table):
        return Table(self._data + other_table.get_data())

    def append_columns(self, other_table):
        return Table([self._data[i] + other_table.get_data()[i] for i in range(len(self._data))])

    def select_columns(self, fields):
        return Table([[row[i] for i in fields] for row in self._data])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self._data])


def load_table(file_path, delimiter='\t'):
    try:
        with open(file_path, 'r') as file:
            return Table([line.strip().split(delimiter) for line in file.readlines()])
    except OSError as e:
        e.strerror = f'An error occurred while loading the table: {e.strerror}'
        raise e


def main():
    parser = argparse.ArgumentParser(description="Utility for working with tables")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    head_parser = subparsers.add_parser("head", help="Get first N rows of the table")
    head_parser.add_argument("-n", type=int, default=1, help="Number of rows")
    head_parser.add_argument("file", type=str, help="Path to the file containing the table")

    tail_parser = subparsers.add_parser("tail", help="Get last N rows of the table")
    tail_parser.add_argument("-n", type=int, default=1, help="Number of rows")
    tail_parser.add_argument("file", type=str, help="Path to the file containing the table")

    cut_parser = subparsers.add_parser("cut", help="Get selected columns from the table")
    cut_parser.add_argument("-f", type=str, required=True, help="Comma-separated list of column indices")
    cut_parser.add_argument("file", type=str, help="Path to the file containing the table")

    paste_parser = subparsers.add_parser("paste", help="Append columns from tables")
    paste_parser.add_argument("files", type=str, nargs=2, help="Paths to the files containing the tables to append")

    args = parser.parse_args()
    try:
        if args.command == "paste":
            tables = [load_table(file) for file in args.files]
            print(tables[0].append_columns(tables[1]))
        else:
            table = load_table(args.file)
            if args.command == "head":
                print(table.head(args.n))
            elif args.command == "tail":
                print(table.tail(args.n))
            elif args.command == "cut":
                fields = list(map(int, args.f.split(',')))
                print(table.select_columns(fields))
    except OSError as e:
        sys.stderr.write(e.strerror)
        exit(1)
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        sys.stderr.write(repr(e))
        exit(1)


if __name__ == "__main__":
    main()
