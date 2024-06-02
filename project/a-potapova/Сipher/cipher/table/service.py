from cipher.core.entity.language import Language
from cipher.core.service import CipherService
from cipher.table.cipher import TableCipher
from cipher.table.decrypter import FrequencyDecrypter
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText


class TableCipherService(CipherService):
    @staticmethod
    def keygen(language: str, **kwargs) -> str:
        language = Language(language)
        return str(TableCipher.keygen(language))

    @staticmethod
    def encode(plaintext: str, key: str = None) -> str:
        text = TableText(plaintext)
        if key is None or key == "":
            ciphertext = text
        else:
            table_key = TableKey(key)
            ciphertext = TableCipher.encrypt(text, key=table_key)
        return str(ciphertext)

    @staticmethod
    def decode(ciphertext: str, key: str = None) -> tuple[str, str]:
        text = TableText(ciphertext)
        if key is None or key == "":
            plaintext, table_key = FrequencyDecrypter.decode(text)
        else:
            table_key = TableKey(key)
            plaintext = TableCipher.decrypt(text, key=table_key)
        return str(plaintext), str(table_key)
