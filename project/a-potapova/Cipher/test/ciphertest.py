import unittest

from cipher.core.entity.language import Language, define_language
from cipher.table.cipher import TableCipher
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText


class AffineCipherTest(unittest.TestCase):
    def letters_bijection(self, key: str, language: Language):
        for letter in language.abc:
            self.assertTrue(letter in key)
        for letter in key:
            self.assertTrue(letter in language.abc)

    def letters_surjection(self, text: str, language: Language):
        for letter in text:
            if letter.isalpha():
                self.assertTrue(letter in language.abc)

    def test_define_language(self):
        self.assertEqual(define_language("language"), Language.English)
        self.assertEqual(define_language("язык"), Language.Russian)
        self.assertRaises(ValueError, lambda: define_language("language | язык"))

    def test_keygen(self):
        for language in [Language.English, Language.Russian]:
            key: TableKey = TableCipher.keygen(language)
            self.assertEqual(len(key), len(language.abc))
            self.letters_bijection(str(key), language)

    def test_encrypt(self):
        self.assertRaises(ValueError, lambda: TableCipher.encrypt(TableText('hello world'))._text)
        self.assertEqual(TableCipher.encrypt(TableText('hello world'), key=TableKey("abcwofglijkdmnepqrstuvhxyz"))._text,
                         'lodde herdw')
        self.assertEqual(TableCipher.encrypt(TableText('aaazzz'), key=TableKey("zbcdefghijklmnopqrstuvwxya"))._text, 'zzzaaa')
        key: TableKey = TableCipher.keygen(Language.English)
        text = TableText('hello world')
        encrypted_text = TableCipher.encrypt(text, key=key)
        self.letters_surjection(str(encrypted_text), Language.English)

    def test_decrypt(self):
        self.assertRaises(ValueError, lambda: TableCipher.decrypt(TableText('hello world'))._text)
        self.assertEqual(TableCipher.decrypt(TableText('lodde herdw'), key=TableKey("abcwofglijkdmnepqrstuvhxyz"))._text, 'hello world')
        key: TableKey = TableCipher.keygen(Language.English)
        text = TableText('hello world')
        decrypted_text = TableCipher.decrypt(text, key=key)
        self.letters_surjection(str(decrypted_text), Language.English)

    def test_all(self):
        for language in [Language.English, Language.Russian]:
            if language == Language.English:
                text = TableText('hello world', language=language)
            else:
                text = TableText('привет мир', language=language)
            for i in range(100):
                key: TableKey = TableCipher.keygen(language)
                encrypted_text = TableCipher.encrypt(text, key=key)
                decrypted_text = TableCipher.decrypt(encrypted_text, key=key)
                self.assertEqual(text, decrypted_text)
                self.letters_surjection(str(encrypted_text), language)
