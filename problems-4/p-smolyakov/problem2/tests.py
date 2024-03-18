import unittest
from pytr import Translator, DifferentAlphabetLengthsException, InvalidAlphabetException


class TranslatorTests(unittest.TestCase):
    def test_regular_case(self):
        tr = Translator('a', 'b')
        self.assertEqual(tr.translate('a'), 'b')


    def test_creation_typeerror(self):
        with self.assertRaises(TypeError):
            tr = Translator(1, 'b', 'c')

        with self.assertRaises(TypeError):
            tr = Translator('a', None, 'c')

        with self.assertRaises(TypeError):
            tr = Translator('a', 'b', ['a', 'b'])

        with self.assertRaises(TypeError):
            tr = Translator(b'abc', 'b', 'c')

    
    def test_creation_invalid_sizes(self):
        with self.assertRaises(DifferentAlphabetLengthsException):
            tr = Translator('abc', 'de')

        with self.assertRaises(DifferentAlphabetLengthsException):
            tr = Translator('abc', 'defg')


    def test_creation_duplicates(self):
        with self.assertRaises(InvalidAlphabetException):
            tr = Translator('abb', 'def')

        with self.assertRaises(InvalidAlphabetException):
            tr = Translator('abc', 'def', tr_remove_alphabet='bb')

    
    def test_translate_typeerror(self):
        tr = Translator('abc', 'dee')
        with self.assertRaises(TypeError):
            tr.translate(b'ab')

    
    def test_translate_noremoval(self):
        tr = Translator('ab', 'cd')
        self.assertEqual(tr.translate('abcd'), 'cdcd')
        self.assertEqual(tr.translate('ab' * 100 + 'c' + 'cd' * 100 + 'd'), 'cd' * 100 + 'c' + 'cd' * 100 + 'd')


    def test_translate_removal(self):
        tr = Translator('abc', 'qwe', 'ad')
        self.assertEqual(tr.translate('abcd'), 'we')
        self.assertEqual(tr.translate('ad' * 100), '')


if __name__ == '__main__':
    unittest.main()
