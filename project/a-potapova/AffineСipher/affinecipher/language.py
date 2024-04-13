import enum


class Language(enum.Enum):
    English = "en", "abcdefghijklmnopqrstuvwxyz"
    Russian = "ru", "абвгдежзийклмнопрстуфхцчшщъыьэюяѐё"

    def get_first_letter(self):
        return self.value[0]

    def get_abc(self) -> str:
        language, abc = self.value
        return abc

    def get_name(self) -> str:
        language, abc = self.value
        return language

    @classmethod
    def _missing_(cls, value):
        if value == "en":
            return cls.English
        if value == "ru":
            return cls.Russian
        else:
            return None


def define_language(text: str) -> Language:
    languages = []
    if any(char.isalpha() and char.lower() in Language.English.get_abc() for char in text):
        languages.append(Language.English)
    if any(char.isalpha() and char.lower() in Language.Russian.get_abc() for char in text):
        languages.append(Language.Russian)
    if len(languages) == 1:
        return languages[0]
    else:
        raise ValueError(f"Unknown language or unexpected languages number: {languages}")
