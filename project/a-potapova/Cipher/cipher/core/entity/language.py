import enum


class Language(enum.Enum):
    """Enum for language."""
    English = "en", "abcdefghijklmnopqrstuvwxyz"
    Russian = "ru", "абвгдежзийклмнопрстуфхцчшщъыьэюяё"

    @property
    def name(self) -> str:
        """Return the language name."""
        language, abc = self.value
        return language

    @property
    def abc(self) -> str:
        """Returns a string with alphabet of the language."""
        language, abc = self.value
        return abc

    @classmethod
    def _missing_(cls, value):
        if value == "en":
            return cls.English
        if value == "ru":
            return cls.Russian
        else:
            return None


def define_language(text: str) -> Language:
    """Defines a language using the given text. Returns enum Language"""
    languages = []
    if any(char.isalpha() and char.lower() in Language.English.abc for char in text):
        languages.append(Language.English)
    if any(char.isalpha() and char.lower() in Language.Russian.abc for char in text):
        languages.append(Language.Russian)
    if len(languages) == 1:
        return languages[0]
    else:
        raise ValueError(f"Unknown language or unexpected languages number: {languages}")
