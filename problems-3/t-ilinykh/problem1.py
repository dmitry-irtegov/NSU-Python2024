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
        return Table(self.data + other.data)

    def concat_columns(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Tables must have the same number of rows")
        return Table([row1 + row2 for row1, row2 in zip(self.data, other.data)])

    def select_columns(self, indices):
        return Table([[row[i] for i in indices] for row in self.data])

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

class TestTable(unittest.TestCase):
    def setUp(self):
        self.data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.data2 = [[10, 11], [12, 13], [14, 15]]
        self.table1 = Table(self.data1)
        self.table2 = Table(self.data2)

    def test_tail(self):
        self.assertEqual(str(self.table1.tail(1)), "7\t8\t9")

    def test_head(self):
        self.assertEqual(str(self.table1.head(2)), "1\t2\t3\n4\t5\t6")

    def test_select_rows(self):
        self.assertEqual(str(self.table1.select_rows([0, 2])), "1\t2\t3\n7\t8\t9")

    def test_concat_rows(self):
        self.assertEqual(str(self.table1.concat_rows(self.table2)), "1\t2\t3\n4\t5\t6\n7\t8\t9\n10\t11\n12\t13\n14\t15")

    def test_concat_columns(self):
        self.assertEqual(str(self.table1.concat_columns(self.table2)), "1\t2\t3\t10\t11\n4\t5\t6\t12\t13\n7\t8\t9\t14\t15")

    def test_select_columns(self):
        self.assertEqual(str(self.table1.select_columns([0, 2])), "1\t3\n4\t6\n7\t9")

if __name__ == "__main__":
    unittest.main()
