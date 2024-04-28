import unittest
from table import Table, load_table


class TestTableMethods(unittest.TestCase):
    def setUp(self):
        self.table1 = load_table("test1.tsv")

    def test_head(self):
        head_table = self.table1.head(2)
        expected_output = "1\t2\t3\n4\t5\t6"
        self.assertEqual(str(head_table), expected_output)

    def test_tail(self):
        tail_table = self.table1.tail(2)
        expected_output = "4\t5\t6\n7\t8\t9"
        self.assertEqual(str(tail_table), expected_output)

    def test_paste(self):
        combined_table = self.table1.append_columns(load_table("test2.tsv"))
        expected_output = "1\t2\t3\t0\t0\n4\t5\t6\t0\t0\n7\t8\t9\t0\t0"
        self.assertEqual(str(combined_table), expected_output)

    def test_invalid_paste(self):
        with self.assertRaises(ValueError):
            self.table1.append_columns(load_table("test4.tsv"))

    def test_cut(self):
        selected_table = self.table1.select_columns([0, 2])
        expected_output = "1\t3\n4\t6\n7\t9"
        self.assertEqual(str(selected_table), expected_output)

    def test_invalid_cut(self):
        with self.assertRaises(ValueError):
            self.table1.select_columns([2, 5])

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            load_table("test3.tsv")


if __name__ == '__main__':
    unittest.main()
