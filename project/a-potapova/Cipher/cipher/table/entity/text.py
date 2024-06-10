import re

from cipher.core.entity.language import define_language, Language
from cipher.core.entity.text import Text


class TableText(Text):
    def __init__(self, text: str, language=None):
        if text is None:
            raise ValueError('Text cannot be None')
        self._text = text
        self._language = language if language is not None else define_language(text)

    @property
    def words(self) -> list[str]:
        return re.findall(r'\b[\w’]+\b', self._text)

    @property
    def language(self) -> Language:
        return self._language

    def __str__(self):
        return self._text
