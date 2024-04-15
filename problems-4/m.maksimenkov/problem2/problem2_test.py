import unittest
import problem2 as tr


class TranslateSymbolsTest(unittest.TestCase):

    def testErrors(self):
        with self.assertRaises(ValueError):
            tr.translate("abc", "ab", "b", "g")

    def testValidArgs(self):
        self.assertEqual(tr.translate("abb", "ab", "cx", ""), "cxx")
        self.assertEqual(tr.translate("bbb", "b", "a", ""), "aaa")

    def testDeleteArg(self):
        self.assertEqual(tr.translate("abb", "xy", "zy", "ab"), "")
        self.assertEqual(tr.translate("aaaaa", "a", "b", "a"), "")

    def testEmptyInput(self):
        self.assertEqual(tr.translate("", "ab", "ab", "a"), "")

    def testWithoutTranslate(self):
        self.assertEqual(tr.translate("fdfdre", "ab", "ba", "a"), "fdfdre")

    def testWithoutTranslate2(self):
        self.assertEqual(tr.translate("refdsfeFD", "", "", ""), "refdsfeFD")

    def testPartTranslate(self):
        self.assertEqual(tr.translate("abababbbbaba", "b", "g", ""), "agagaggggaga")

    def testPartTranslateWithDelete(self):
        self.assertEqual(tr.translate("abbgbbgda", "a", "z", "b"), "zggdz")



