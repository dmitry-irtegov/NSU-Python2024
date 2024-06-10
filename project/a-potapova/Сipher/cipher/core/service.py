from abc import ABC, abstractmethod
from typing import Any
from fastapi import status

from cipher.core.entity.language import Language


class CipherService(ABC):
    """Abstract base class for cipher services"""

    @abstractmethod
    def keygen(self, language: Language, **kwargs) -> str:
        """Generate a random key for the given language. Returns the key"""
        pass


    @abstractmethod
    def encode(self, plaintext: str, key=None) -> str:
        """Encode the given text to the given key. Returns the encoded text"""
        pass


    @abstractmethod
    def decode(self, ciphertext: str, timeout: float, key=None) -> tuple[str, Any, status]:
        """Decode the given text to the given key. Returns the decoded text and key"""
        pass
