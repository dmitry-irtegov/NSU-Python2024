import unittest
from affinecipher.core.ciphers.cipher import Cipher
from affinecipher.core.ciphers.affinecipher import AffineCipher
from affinecipher.language import Language, define_language


class AffineCipherTest(unittest.TestCase):
    def letters_bijection(self, key: str, language: Language):
        for letter in language.get_abc():
            self.assertTrue(letter in key)
        for letter in key:
            self.assertTrue(letter in language.get_abc())

    def letters_surjection(self, text: str, language: Language):
        for letter in text:
            if letter.isalpha():
                self.assertTrue(letter in language.get_abc())

    def test_define_language(self):
        self.assertEqual(define_language("language"), Language.English)
        self.assertEqual(define_language("язык"), Language.Russian)
        self.assertRaises(ValueError, lambda: define_language("language | язык"))

    def test_keygen(self):
        for language in [Language.English, Language.Russian]:
            key: str = AffineCipher.keygen(language)
            self.assertEqual(len(key), len(language.get_abc()))
            self.letters_bijection(key, language)

    def test_encrypt(self):
        cipher: Cipher = AffineCipher(Language.English)
        self.assertEqual(cipher.encrypt('hello world'), 'hello world')
        self.assertEqual(cipher.encrypt('hello world', key="abcwofglijkdmnepqrstuvhxyz"), 'lodde herdw')
        self.assertEqual(cipher.encrypt('aaazzz', key="zbcdefghijklmnopqrstuvwxya"), 'zzzaaa')
        key: str = AffineCipher.keygen(Language.English)
        text = 'hello world'
        encrypted_text = cipher.encrypt(text, key=key)
        self.letters_surjection(encrypted_text, Language.English)

    def test_decrypt(self):
        cipher: Cipher = AffineCipher(Language.English)
        self.assertEqual(cipher.decrypt('hello world'), 'hello world')
        self.assertEqual(cipher.decrypt('lodde herdw', key="abcwofglijkdmnepqrstuvhxyz"), 'hello world')
        key: str = AffineCipher.keygen(Language.English)
        text = 'hello world'
        decrypted_text = cipher.decrypt(text, key=key)
        self.letters_surjection(decrypted_text, Language.English)

    def test_all(self):
        cipher: Cipher = AffineCipher(Language.English)
        for language in [Language.English, Language.Russian]:
            if language == Language.English:
                text = 'hello world'
            elif language == Language.Russian:
                text = 'привет мир'
            else:
                text = ''
            for i in range(100):
                key: str = AffineCipher.keygen(language)

                encrypted_text = cipher.encrypt(text, key=key)
                decrypted_text = cipher.decrypt(encrypted_text, key=key)
                self.assertEqual(text, decrypted_text)
                self.letters_surjection(encrypted_text, language)
