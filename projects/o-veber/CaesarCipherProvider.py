from string import ascii_lowercase


class CaesarCipherProvider:
    def __init__(self):
        self._provided_languages = [
            Language('ru', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'),
            Language('en', ascii_lowercase)
        ]

    def find_language(self, name):
        for language in self._provided_languages:
            if language.get_name() == name:
                return language
        raise ValueError(f"Unexpected language with name {name}")

    def decode(self, text, shift, language):
        alphabet = language.get_alphabet()
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        return text.translate(table)


class Language:
    def __init__(self, name, alphabet):
        self._name = name
        self._alphabet = alphabet
        self._alphabet_power = len(alphabet)

    def get_name(self):
        return self._name

    def get_alphabet(self):
        return self._alphabet

    def get_alphabet_power(self):
        return self._alphabet_power
