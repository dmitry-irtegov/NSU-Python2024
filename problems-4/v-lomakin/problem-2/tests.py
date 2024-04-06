from tr import tr
import unittest

class TestTr (unittest.TestCase):
    def test_empty(self):
        self.assertEqual(tr("", "abc", "qwe", "ad"), "")

    def test_example(self):
        self.assertEqual(tr("abcd", "abc", "qwe", "ad"), "we")

    def test_error(self):
        with self.assertRaises(ValueError) as ve:
            tr("", "", "s")
        self.assertEqual(str(ve.exception), "Строки замены и заменяемые строки должны быть одинаковой длины")

    def test_error2(self):
        with self.assertRaises(ValueError) as ve:
            tr("", "bb", "se")
        self.assertEqual(str(ve.exception),"Заменяемые символы не должны повторяться") 

    def test_equal(self):
        self.assertEqual(tr("ex", "", ""), "ex")

    def test_equalArgs(self):
        self.assertEqual(tr("abcd", "abe", "abe"), "abcd")

    def test_deleteNothing(self):
        self.assertEqual(tr("abcd", "ab", "cd", ""), "cdcd")

    def test_oneLetter(self):
        self.assertEqual(tr("bbbbbbbbbbb", "b", "C"), "CCCCCCCCCCC")

if __name__ == "__main__":
    unittest.main()
