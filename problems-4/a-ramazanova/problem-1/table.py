import argparse
import sys


class Table:
    def __init__(self, data):
        self._data = data
        self._validate_data()

    def get_data(self):
        return self._data

    def _validate_data(self):
        if not isinstance(self._data, list) or not all(isinstance(row, list) for row in self._data):
            sys.stderr.write("Table data must be a list of lists")
        if self._data:
            row_len = len(self._data[0])
            if any(len(row) != row_len for row in self._data):
                sys.stderr.write("All rows in the table must have the same length")

    def head(self, n):
        return Table(self._data[:n])

    def tail(self, n):
        return Table(self._data[-n:])

    def select_rows(self, indices):
        if any(i >= len(self._data) for i in indices):
            sys.stderr.write(f'Row id must be >= {len(self._data)}')
        selected_rows = [self._data[i] for i in indices if i < len(self._data)]
        return Table(selected_rows)

    def append_rows(self, other_table):
        new_data = self._data + other_table.get_data()
        return Table(new_data)

    def append_columns(self, other_table):
        if len(self._data) != len(other_table.get_data()):
            sys.stderr.write("Tables must have the same number of rows")
        else:
            combined_data = [self._data[i] + other_table.get_data()[i] for i in range(len(self._data))]
            return Table(combined_data)

    def select_columns(self, fields):
        if any(i >= len(self._data) for i in fields):
            sys.stderr.write(f'Column id must be >= {len(self._data)}')
        else:
            return Table([[row[i] for i in fields] for row in self._data])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self._data])


def load_table(file_path, delimiter='\t'):
    try:
        file = open(file_path, 'r')
    except Exception as e:
        sys.stderr.write(f'Error with open file: {e}')
        exit(1)
    else:
        with file:
            data = [line.strip().split(delimiter) for line in file.readlines()]
        return Table(data)


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

    if args.command == "head":
        table = load_table(args.file)
        print(table.head(args.n))
    elif args.command == "tail":
        table = load_table(args.file)
        print(table.tail(args.n))
    elif args.command == "cut":
        table = load_table(args.file)
        fields = list(map(int, args.f.split(',')))
        print(table.select_columns(fields))
    elif args.command == "paste":
        tables = [load_table(file) for file in args.files]
        print(tables[0].append_columns(tables[1]))


if __name__ == "__main__":
    main()
