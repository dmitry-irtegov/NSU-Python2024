from abc import ABC, abstractmethod
from fastapi import status
from cipher.core.entity.text import Text


class Decrypter(ABC):
    """Interface for decrypters. Decrypter decodes cipher text without a key."""
    @abstractmethod
    async def decode(self, text: Text) -> tuple[Text, status]:
        """Decrypts cipher text without a key."""
        pass
