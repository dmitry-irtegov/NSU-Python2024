import random

from cipher.core.entity.language import Language
from cipher.core.cipher import Cipher
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText

"""Table cipher"""


class TableCipher(Cipher):
    @staticmethod
    def encrypt(plaintext: TableText, key: TableKey = None) -> TableText:
        if key is None:
            raise ValueError("Key must be provided")
        table = key.table
        return TableText(''.join((table[char.lower()]
                                  if char.islower() else table[char.lower()].capitalize())
                                 if char.isalpha() else char
                                 for char in str(plaintext)),
                         language=plaintext.language)

    @staticmethod
    def decrypt(ciphertext: TableText, key: TableKey = None) -> TableText:
        if key is None:
            raise ValueError("Key must be provided")
        table = key.reversed()
        return TableText(''.join((table[char.lower()]
                                  if char.islower() else table[char.lower()].capitalize())
                                 if char.isalpha() else char
                                 for char in str(ciphertext)),
                         language=ciphertext.language)

    @staticmethod
    def keygen(language: Language) -> TableKey:
        return TableKey(''.join(random.sample(language.abc, len(language.abc))), language=language)
