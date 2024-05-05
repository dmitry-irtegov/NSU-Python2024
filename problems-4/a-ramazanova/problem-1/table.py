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
            raise ValueError("Table data must be a list of lists")
        if self._data:
            row_len = len(self._data[0])
            if any(len(row) != row_len for row in self._data):
                raise ValueError("All rows in the table must have the same length")

    def head(self, n):
        return Table(self._data[:n])

    def tail(self, n):
        return Table(self._data[-n:])

    def select_rows(self, indices):
        if any(i >= len(self._data) for i in indices):
            raise ValueError(f'Id must be < {len(self._data)}')
        selected_rows = [self._data[i] for i in indices if i < len(self._data)]
        return Table(selected_rows)

    def append_rows(self, other_table):
        new_data = self._data + other_table.get_data()
        return Table(new_data)

    def append_columns(self, other_table):
        if len(self._data) != len(other_table.get_data()):
            raise ValueError("Tables must have the same number of rows")
        combined_data = [self._data[i] + other_table.get_data()[i] for i in range(len(self._data))]
        return Table(combined_data)

    def select_columns(self, fields):
        if any(i >= len(self._data[0]) for i in fields):
            raise ValueError(f'Fields must be < {len(self._data[0])}')
        return Table([[row[i] for i in fields] for row in self._data])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self._data])


def load_table(file_path, delimiter='\t'):
    try:
        with open(file_path, 'r') as file:
            data = [line.strip().split(delimiter) for line in file.readlines()]
        return Table(data)
    except Exception:
        raise


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

    if args.command == "paste":
        try:
            tables = [load_table(file) for file in args.files]
        except Exception as e:
            sys.stderr.write(f'An error occurred while loading the tables: {e}')
        else:
            try:
                print(tables[0].append_columns(tables[1]))
            except Exception as e:
                sys.stderr.write(f'An error occurred while appending the tables: {e}')
    else:
        try:
            table = load_table(args.file)
        except Exception as e:
            sys.stderr.write(f'An error occurred while loading the table: {e}')
            exit(1)
        if args.command == "head":
            print(table.head(args.n))
        elif args.command == "tail":
            print(table.tail(args.n))
        elif args.command == "cut":
            fields = list(map(int, args.f.split(',')))
            try:
                print(table.select_columns(fields))
            except Exception as e:
                sys.stderr.write(f'An error occurred while selecting column: {e}')


if __name__ == "__main__":
    main()
