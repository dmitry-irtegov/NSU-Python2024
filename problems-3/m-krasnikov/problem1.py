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

    def join_rows(self, other_table):
        new_data = self.data.extend(other_table.data)
        return Table(new_data)

    def join_columns(self, other_table):
        if len(self.data) != len(other_table.data):
            raise ValueError("Tables must have the same number of rows to join columns.")

        new_data = [self.data[row].extend(other_table.data[row]) for row in range(len(self.data))]
        return Table(new_data)

    def select_columns(self, column_indices):
        new_data = [[row[i] for i in column_indices] for row in self.data]
        return Table(new_data)

    def __repr__(self):
        return "\n".join(map(str, self.data))


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table1 = Table([
            ["Name", "Age", "Gender"],
            ["Alice", 30, "Female"],
            ["Bob", 25, "Male"],
            ["Charlie", 35, "Male"]
        ])
        self.table2 = Table([
            ["City", "Country"],
            ["New York", "USA"],
            ["London", "UK"],
            ["Paris", "France"]
        ])

    def test_head(self):
        self.assertListEqual(
            [["Name", "Age", "Gender"],
             ["Alice", 30, "Female"]],
            self.table1.head(2).data)

    def test_tail(self):
        self.assertListEqual(
            [["Charlie", 35, "Male"]],
            self.table1.tail(1).data)

    def test_get_row(self):
        self.assertListEqual(
            ["Alice", 30, "Female"],
            self.table1.get_row(1))

    def test_join_rows(self):
        self.table1.join_rows(self.table2)
        self.assertListEqual(
            [["Name", "Age", "Gender"],
             ["Alice", 30, "Female"],
             ["Bob", 25, "Male"],
             ["Charlie", 35, "Male"], ["City", "Country"],
             ["New York", "USA"],
             ["London", "UK"],
             ["Paris", "France"]],
            self.table1.data
        )

    def test_join_columns(self):
        self.table1.join_columns(self.table2)
        self.assertListEqual(
            [["Name", "Age", "Gender", "City", "Country"],
             ["Alice", 30, "Female", "New York", "USA"],
             ["Bob", 25, "Male", "London", "UK"],
             ["Charlie", 35, "Male", "Paris", "France"]],
            self.table1.data
        )

    def test_select_columns(self):
        selected_columns = self.table1.select_columns([0, 2])
        self.assertListEqual(
            [["Name", "Gender"],
             ["Alice", "Female"],
             ["Bob", "Male"],
             ["Charlie", "Male"]],
            selected_columns.data)


if __name__ == "__main__":
    unittest.main()
