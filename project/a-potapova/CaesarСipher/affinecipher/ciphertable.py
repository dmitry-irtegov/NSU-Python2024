from uvicorn.config import logger


def count_encrypt_shifts(key: str) -> list:
    result = [0] * len(key)
    for i, char in enumerate(key):
        result[i] = ord(char) - ord('a') - i
    logger.info(f"Encrypt: {[str(r) for r in result]}")
    return result


def count_decrypt_shifts(key: str) -> list:
    result = [0] * len(key)
    for i, char in enumerate(key):
        result[ord(char) - ord('a')] = i - (ord(char) - ord('a'))
    logger.info(f"Decrypt: {[str(r) for r in result]}")
    return result


class CipherTable:
    def __init__(self, key: str):
        self.encrypt_shifts = count_encrypt_shifts(key)
        self.decrypt_shifts = count_decrypt_shifts(key)

    def encrypt(self, char: str) -> str:
        return chr(ord(char) + self.encrypt_shifts[ord(char.lower()) - ord('a')])

    def decrypt(self, char: str) -> str:
        return chr(ord(char) + self.decrypt_shifts[ord(char.lower()) - ord('a')])
