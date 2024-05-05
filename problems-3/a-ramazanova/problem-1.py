import unittest


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
        self.assertEqual(self.valid_table._data, self.valid_data)

    def test_head(self):
        head_table = self.valid_table.head(2)
        expected_data = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.assertEqual(head_table._data, expected_data)

    def test_tail(self):
        tail_table = self.valid_table.tail(2)
        expected_data = [
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(tail_table._data, expected_data)

    def test_select_rows(self):
        selected_rows_table = self.valid_table.select_rows([0, 2])
        expected_data = [
            [1, 2, 3],
            [7, 8, 9]
        ]
        self.assertEqual(selected_rows_table._data, expected_data)

    def test_append_rows(self):
        other_table = Table([[10, 11, 12]])
        appended_table = self.valid_table.append_rows(other_table)
        expected_data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]
        self.assertEqual(appended_table._data, expected_data)

    def test_append_columns(self):
        other_table = Table([[10], [11], [12]])
        appended_table = self.valid_table.append_columns(other_table)
        expected_data = [
            [1, 2, 3, 10],
            [4, 5, 6, 11],
            [7, 8, 9, 12]
        ]
        self.assertEqual(appended_table._data, expected_data)

    def test_select_columns(self):
        selected_columns_table = self.valid_table.select_columns([0, 2])
        expected_data = [
            [1, 3],
            [4, 6],
            [7, 9]
        ]
        self.assertEqual(selected_columns_table._data, expected_data)

    def test_select_invalid_columns(self):
        with self.assertRaises(ValueError):
            self.valid_table.select_columns([2, 5])

    def test_select_invalid_row(self):
        with self.assertRaises(ValueError):
            self.valid_table.select_rows([2, 5])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            Table(self.invalid_data)

    def test_invalid_data2(self):
        with self.assertRaises(ValueError):
            Table("sfesf")


if __name__ == '__main__':
    unittest.main()
