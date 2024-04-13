from uvicorn.config import logger

from affinecipher.language import define_language


class CipherTable:
    def __init__(self, key: str):
        language = define_language(key)
        self.ord_first_letter = ord(language.get_abc()[0])
        self.ord_last_letter = ord(language.get_abc()[-1])
        self.abc_length = len(language.get_abc())
        self.encrypt_shifts = self.count_encrypt_shifts(key)
        self.decrypt_shifts = self.count_decrypt_shifts(key)

    def normalize(self, value: int):
        return value % self.abc_length - self.abc_length

    def count_encrypt_shifts(self, key: str) -> []:
        result = [0] * len(key)
        for i, char in enumerate(key):
            result[i] = ord(char) - self.ord_first_letter - i
        logger.info(f"Encrypt: {[str(r) for r in result]}")
        return result

    def count_decrypt_shifts(self, key: str) -> []:
        result = [0] * len(key)
        for i, char in enumerate(key):
            result[ord(char) - self.ord_first_letter] = i - (ord(char) - self.ord_first_letter)
        logger.info(f"Decrypt: {[str(r) for r in result]}")
        return result

    def encrypt(self, char: str) -> str:
        return chr(ord(char) + self.encrypt_shifts[ord(char.lower()) - self.ord_first_letter])

    def decrypt(self, char: str) -> str:
        return chr(ord(char) + self.decrypt_shifts[ord(char.lower()) - self.ord_first_letter])
