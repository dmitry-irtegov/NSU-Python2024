import random

from affinecipher.language import Language
from .cipher import Cipher
from .ciphertable import CipherTable


class AffineCipher(Cipher):
    def __init__(self, key):
        self.table = CipherTable(key)

    def set_key(self, key):
        self.table = CipherTable(key)

    @staticmethod
    def keygen(language: Language):
        language = language.get_abc()
        return ''.join(random.sample(language, len(language)))

    def encrypt(self, text: str, key: str = None) -> str:
        if key is not None:
            self.set_key(key)
        return ''.join(self.table.encrypt(char) if char.isalpha() else char for char in text)

    def decrypt(self, text: str, key: str = None) -> str:
        if key is not None:
            self.set_key(key)
        return ''.join(self.table.decrypt(char) if char.isalpha() else char for char in text)
