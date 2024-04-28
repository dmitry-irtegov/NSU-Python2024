import unittest


class Table:
    def __init__(self, data):
        self.data = data
        self._validate_data()

    def _validate_data(self):
        if not all(isinstance(row, list) for row in self.data):
            raise ValueError("Table data must be a list of lists")
        if len(set(len(row) for row in self.data)) != 1:
            raise ValueError("All rows in the table must have the same length")

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        return Table(self.data[-n:])

    def select_rows(self, indices):
        if any(i >= len(self.data) for i in indices):
            raise ValueError("No such row in table")
        selected_rows = [self.data[i] for i in indices if i < len(self.data)]
        return Table(selected_rows)

    def append_rows(self, other_table):
        new_data = self.data + other_table.data
        return Table(new_data)

    def append_columns(self, other_table):
        if len(self.data) != len(other_table.data):
            raise ValueError("Tables must have the same number of rows")
        combined_data = [self.data[i] + other_table.data[i] for i in range(len(self.data))]
        return Table(combined_data)

    def select_columns(self, fields):
        if any(i >= len(self.data) for i in fields):
            raise ValueError('no such column in table')
        return Table([[row[i] for i in fields] for row in self.data])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


class TestTable(unittest.TestCase):
    def setUp(self):
        self.valid_data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.valid_table = Table(self.valid_data)

        self.invalid_data = [
            [1, 2, 3],
            [4, 5],
            [7, 8, 9]
        ]

    def test_valid_data(self):
        self.assertEqual(self.valid_table.data, self.valid_data)

    def test_head(self):
        head_table = self.valid_table.head(2)
        expected_data = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.assertEqual(head_table.data, expected_data)

    def test_tail(self):
        tail_table = self.valid_table.tail(2)
        expected_data = [
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(tail_table.data, expected_data)

    def test_select_rows(self):
        selected_rows_table = self.valid_table.select_rows([0, 2])
        expected_data = [
            [1, 2, 3],
            [7, 8, 9]
        ]
        self.assertEqual(selected_rows_table.data, expected_data)

    def test_append_rows(self):
        other_table = Table([[10, 11, 12]])
        appended_table = self.valid_table.append_rows(other_table)
        expected_data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
        self.assertEqual(appended_table.data, expected_data)

    def test_append_columns(self):
        other_table = Table([[10], [11], [12]])
        appended_table = self.valid_table.append_columns(other_table)
        expected_data = [
            [1, 2, 3, 10],
            [4, 5, 6, 11],
            [7, 8, 9, 12]
        ]
        self.assertEqual(appended_table.data, expected_data)

    def test_select_columns(self):
        selected_columns_table = self.valid_table.select_columns([0, 2])
        expected_data = [
            [1, 3],
            [4, 6],
            [7, 9]
        ]
        self.assertEqual(selected_columns_table.data, expected_data)

    def test_select_invalid_columns(self):
        with self.assertRaises(ValueError):
            self.valid_table.select_columns([2, 5])

    def test_select_invalid_row(self):
        with self.assertRaises(ValueError):
            self.valid_table.select_columns([2, 5])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Table(self.invalid_data)


if __name__ == '__main__':
    unittest.main()
