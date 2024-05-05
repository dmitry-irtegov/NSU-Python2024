from string import ascii_lowercase as en_lowercase, ascii_uppercase as en_uppercase
from enum import Enum


class CaesarCipherProvider:
    def __init__(self):
        ru_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        ru_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЩЩЗЪЫЬЭЮЯ'
        self._provided_languages = [
            Language('ru', [ru_lowercase, ru_uppercase], 33),
            Language('en', [en_lowercase, en_uppercase], 22)
        ]

    def find_language(self, name):
        for language in self._provided_languages:
            if language.get_name() == name:
                return language
        raise ValueError(f"Unexpected language with name {name}")

    def translate(self, letter, shift, language, shift_type):
        alphabets = language.get_alphabets()
        for alphabet in alphabets:
            if letter in alphabet:
                index = alphabet.index(letter)
                new_index = index + shift if shift_type == ShiftType.ENCODE else index - shift
                new_index = new_index % language.get_power()
                return alphabet[new_index]
        return letter

    def get_text_with_shift_for_language_name(self, text, shift, lang_name, shift_type):
        return self.get_text_with_shift_for_language(text, shift, self.find_language(lang_name), shift_type)

    def get_text_with_shift_for_language(self, text, shift, language, shift_type):
        new_text = [None] * len(text)
        for i, letter in enumerate(text):
            new_text[i] = self.translate(letter, shift, language, shift_type)

        return ''.join(new_text)


class ShiftType(Enum):
    ENCODE = 1,
    DECODE = 2


class Language:
    def __init__(self, name, alphabets, alphabet_power):
        self._name = name
        self._alphabets = alphabets
        self._alphabet_power = alphabet_power

    def get_name(self):
        return self._name

    def get_alphabets(self):
        return self._alphabets

    def get_power(self):
        return self._alphabet_power


class Alphabet:
    def __init__(self, alphabet_symbols):
        self._alphabet_symbols = alphabet_symbols

    def get_alphabet_symbols(self):
        return self._alphabet_symbols
