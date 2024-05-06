import unittest
from main import Table


class TestTableInit(unittest.TestCase):
    def test_null(self) -> None:
        table: Table = Table(3, 15)
        self.assertEqual(table.rows, 3)
        self.assertEqual(table.columns, 15)
        self.assertEqual(table.table, [[None] * 15] * 3)

    def test_common(self) -> None:
        matrix: list[list[float]] = [[12.3, 13.4, 5.6], [1.5, 2.5, 6.5]]
        table: Table[float] = Table(2, 3, matrix)
        self.assertEqual(table.rows, 2)
        self.assertEqual(table.columns, 3)
        self.assertEqual(table.table, matrix)


class TestTableTail(unittest.TestCase):
    def test(self) -> None:
        table: Table = Table(4, 2, [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]])
        expected: list[list[float]] = [[3.3, 4.4], [5.5, 6.6], [7.7, 8.8]]
        result = table.tail(3)
        self.assertEqual(3, result.rows)
        self.assertEqual(2, result.columns)
        self.assertEqual(expected, result.table)

class TestTableHead(unittest.TestCase):
    def test(self) -> None:
        table: Table = Table(4, 2, [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]])
        expected: list[list[float]] = [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]]
        result = table.head(3)
        self.assertEqual(3, result.rows)
        self.assertEqual(2, result.columns)
        self.assertEqual(expected, result.table)


class TestTableSelectRows(unittest.TestCase):
    def test(self) -> None:
        table: Table = Table(4, 2, [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]])
        expected: list[list[float]] = [[3.3, 4.4], [7.7, 8.8]]
        result = table.select_rows(1, 3)
        self.assertEqual(2, result.rows)
        self.assertEqual(2, result.columns)
        self.assertEqual(expected, result.table)


class TestTableSelectColumns(unittest.TestCase):
    def test(self) -> None:
        table: Table = Table(2, 4, [[1.1, 2.2, 3.3, 4.4], [5.5, 6.6, 7.7, 8.8]])
        expected: list[list[float]] = [[1.1, 3.3], [5.5, 7.7]]
        result = table.select_columns(0, 2)
        self.assertEqual(2, result.rows)
        self.assertEqual(2, result.columns)
        self.assertEqual(expected, result.table)


class TestTableJoinRows(unittest.TestCase):
    def test(self) -> None:
        table1: Table = Table(3, 2, [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]])
        table2: Table = Table(2, 2, [[7.7, 8.8], [9.9, 10.11]])
        expected: list[list[float]] = [[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8], [9.9, 10.11]]
        result = table1.join_rows(table2)
        self.assertEqual(5, result.rows)
        self.assertEqual(2, result.columns)
        self.assertEqual(expected, result.table)


class TestTableJoinColumns(unittest.TestCase):
    def test(self) -> None:
        table1: Table = Table(2, 3, [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
        table2: Table = Table(2, 2, [[7.7, 8.8], [9.9, 10.11]])
        expected: list[list[float]] = [[1.1, 2.2, 3.3, 7.7, 8.8], [4.4, 5.5, 6.6, 9.9, 10.11]]
        result = table1.join_columns(table2)
        self.assertEqual(2, result.rows)
        self.assertEqual(5, result.columns)
        self.assertEqual(expected, result.table)


if __name__ == "__main__":
    unittest.main()
