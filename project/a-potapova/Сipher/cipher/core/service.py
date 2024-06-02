from abc import ABC, abstractmethod
from typing import Any

from cipher.core.entity.language import Language


class CipherService(ABC):
    """Abstract base class for cipher services"""
    @staticmethod
    @abstractmethod
    def keygen(language: Language, **kwargs) -> str:
        """Generate a random key for the given language. Returns the key"""
        pass

    @staticmethod
    @abstractmethod
    def encode(plaintext: str, key=None) -> str:
        """Encode the given text to the given key. Returns the encoded text"""
        pass

    @staticmethod
    @abstractmethod
    def decode(ciphertext: str, key=None) -> tuple[str, Any]:
        """Decode the given text to the given key. Returns the decoded text and key"""
        pass
