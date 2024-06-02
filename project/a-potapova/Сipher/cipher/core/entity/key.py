from abc import ABC, abstractmethod

from cipher.core.entity.language import Language


class Key(ABC):
    """Class for key."""

    @abstractmethod
    def __str__(self) -> str:
        """Returns a string representation of the key."""
        pass

    @property
    @abstractmethod
    def language(self) -> Language:
        """Returns a language of the key."""
        pass
