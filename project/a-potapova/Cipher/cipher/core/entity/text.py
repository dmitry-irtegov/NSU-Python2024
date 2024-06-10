from abc import ABC, abstractmethod

from cipher.core.entity.language import Language


class Text(ABC):
    """Class for text."""

    @abstractmethod
    def __init__(self, text: str, language=None):
        pass

    @property
    @abstractmethod
    def language(self) -> Language:
        """Returns a language of text."""
        pass

    @abstractmethod
    def __str__(self):
        """Returns a string representation of the text."""
        pass

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__str__() == other.__str__()

