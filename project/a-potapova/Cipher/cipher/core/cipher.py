from abc import ABC, abstractmethod
from typing import Any

from cipher.core.entity.text import Text


class Cipher(ABC):
    """Interface for ciphers."""
    @staticmethod
    @abstractmethod
    def keygen(**args) -> Any:
        """Generate a random key. Returns key"""
        pass

    @staticmethod
    @abstractmethod
    def encrypt(plaintext: Text, key=None) -> Text:
        """Encrypt a plain text. Returns encrypted text"""
        pass

    @staticmethod
    @abstractmethod
    def decrypt(ciphertext: Text, key=None) -> Text:
        """Decrypt a cipher text. Returns decrypted text"""
        pass
