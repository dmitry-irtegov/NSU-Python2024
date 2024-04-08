import unittest


class Table:
    def __init__(self, data):
        self.data = data

    def tail(self, n):
        return Table(self.data[-n:])

    def head(self, n):
        return Table(self.data[:n])

    def get_row(self, index):
        return self.data[index]

    def append_rows(self, other_table):
        self.data.extend(other_table.data)

    def append_columns(self, other_table):
        if len(self.data) != len(other_table.data):
            raise ValueError("Tables must have the same number of rows")
        for table_row in range(len(self.data)):
            self.data[table_row].extend(other_table.data[table_row])

    def select_columns(self, indices):
        selected_data = []
        for table_row in self.data:
            selected_row = [table_row[i] for i in indices]
            selected_data.append(selected_row)
        return Table(selected_data)


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table1 = Table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.table2 = Table([[10, 11], [12, 13], [14, 15]])

    def test_head(self):
        self.assertListEqual([[1, 2, 3], [4, 5, 6]], self.table1.head(2).data)

    def test_tail(self):
        self.assertListEqual([[7, 8, 9]], self.table1.tail(1).data)

    def test_get_row(self):
        self.assertListEqual([4, 5, 6], self.table1.get_row(1))

    def test_append_rows(self):
        self.table1.append_rows(self.table2)
        self.assertListEqual(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11], [12, 13], [14, 15]],
            self.table1.data
        )

    def test_append_cols(self):
        self.table1.append_columns(self.table2)
        self.assertListEqual(
            [[1, 2, 3, 10, 11], [4, 5, 6, 12, 13], [7, 8, 9, 14, 15]],
            self.table1.data
        )

    def test_select_columns(self):
        selected_columns = self.table1.select_columns([0, 2])
        self.assertListEqual([[1, 3], [4, 6], [7, 9]], selected_columns.data)


if __name__ == "__main__":
    unittest.main()
