from abc import ABC, abstractmethod

from cipher.core.entity.text import Text


class Decrypter(ABC):
    """Interface for decrypters. Decrypter decodes cipher text without a key."""
    @staticmethod
    @abstractmethod
    def decode(text: Text) -> Text:
        """Decrypts cipher text without a key."""
        pass
