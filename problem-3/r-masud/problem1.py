import unittest

class Table:
    def __init__(self, data):
        self.data = data

    def tail(self, n):
        return Table(self.data[-n:])

    def head(self, n):
        return Table(self.data[:n])

    def select_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def concat_rows(self, other):
        new_data = self.data + other.data
        return Table(new_data)

    def concat_columns(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Tables should have the same number of rows")
        new_data = [row1 + row2 for row1, row2 in zip(self.data, other.data)]
        return Table(new_data)

    def select_columns(self, indices):
        new_data = [[row[i] for i in indices] for row in self.data]
        return Table(new_data)

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self.data == other.data

class TestTable(unittest.TestCase):
    def setUp(self):
        self.data1 = [[1, 'apple', 3.5], [4, 'banana', 2.8], [7, 'orange', 4.2]]
        self.data2 = [[10, 'grape'], [12, 'pineapple'], [14, 'watermelon']]
        self.table1 = Table(self.data1)
        self.table2 = Table(self.data2)

    def test_tail(self):
        expected_tail = Table([[4, 'banana', 2.8], [7, 'orange', 4.2]])
        self.assertEqual(self.table1.tail(2).data, expected_tail.data)

    def test_head(self):
        expected_head = Table([[1, 'apple', 3.5]])
        self.assertEqual(self.table1.head(1).data, expected_head.data)

    def test_select_rows(self):
        expected_selected_rows = Table([[1, 'apple', 3.5], [7, 'orange', 4.2]])
        self.assertEqual(self.table1.select_rows([0, 2]).data, expected_selected_rows.data)

    def test_concat_rows(self):
        expected_concatenated_rows = Table([[1, 'apple', 3.5], [4, 'banana', 2.8], [7, 'orange', 4.2], [10, 'grape'], [12, 'pineapple'], [14, 'watermelon']])
        self.table1 = self.table1.concat_rows(self.table2)
        self.assertEqual(self.table1.data, expected_concatenated_rows.data)

    def test_concat_columns(self):
        expected_concatenated_columns = Table([[1, 'apple', 3.5, 10, 'grape'], [4, 'banana', 2.8, 12, 'pineapple'], [7, 'orange', 4.2, 14, 'watermelon']])
        self.table1 = self.table1.concat_columns(self.table2)
        self.assertEqual(self.table1.data, expected_concatenated_columns.data)

    def test_select_columns(self):
        expected_selected_columns = Table([[1, 3.5], [4, 2.8], [7, 4.2]])
        self.assertEqual(self.table1.select_columns([0, 2]).data, expected_selected_columns.data)

if __name__ == "__main__":
    unittest.main()
