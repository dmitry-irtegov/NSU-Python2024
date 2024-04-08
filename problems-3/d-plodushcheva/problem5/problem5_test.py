import unittest
from problem5 import Table


class TestTable(unittest.TestCase):

    def test_head(self):
        data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        table1 = Table(data1)
        self.assertEqual(table1.head(1), Table([[1, 2, 3]]))
        self.assertEqual(table1.head(2), Table([[1, 2, 3], [4, 5, 6]]))

    def test_tail(self):
        data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        table1 = Table(data1)
        self.assertEqual(table1.tail(1), Table([[7, 8, 9]]))
        self.assertEqual(table1.tail(2), Table([[4, 5, 6], [7, 8, 9]]))

    def test_select_rows(self):
        data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        table1 = Table(data1)
        self.assertEqual(table1.select_rows([0, 2]), Table([[1, 2, 3], [7, 8, 9]]))
        self.assertEqual(table1.select_rows([1]), Table([[4, 5, 6]]))

    def test_select_columns(self):
        data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        table1 = Table(data1)
        self.assertEqual(table1.select_columns([0, 2]), Table([[1, 3], [4, 6], [7, 9]]))
        self.assertEqual(table1.select_columns([1]), Table([[2], [5], [8]]))

    def test_concat_rows(self):
        data1 = [[1, 2, 3], [4, 5, 6]]
        table1 = Table(data1)
        data2 = [[10, 11, 12], [13, 14, 15]]
        table2 = Table(data2)
        self.assertEqual(table1.concat_rows(table2), Table([[1, 2, 3], [4, 5, 6], [10, 11, 12], [13, 14, 15]]))

    def test_concat_columns(self):
        data1 = [[1, 2, 3], [4, 5, 6]]
        table1 = Table(data1)
        data2 = [[10, 11, 12], [13, 14, 15]]
        table2 = Table(data2)
        self.assertEqual(table1.concat_columns(table2), Table([[1, 2, 3, 10, 11, 12], [4, 5, 6, 13, 14, 15]]))


if __name__ == '__main__':
    unittest.main()
