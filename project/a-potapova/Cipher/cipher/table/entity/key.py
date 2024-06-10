from copy import copy

from cipher.core.entity.key import Key
from cipher.core.entity.language import Language, define_language


class TableKey(Key):
    """Class for key."""
    def __init__(self, key: str | dict[str, str], language: Language = None):
        if key is None:
            raise ValueError("Key cannot be None")
        elif isinstance(key, str):
            self._key = key
            self._language = language if language is not None else define_language(key)
            self._table = {c: c2 for c, c2 in zip(self._language.abc, key)}
        elif isinstance(key, dict):
            self._table = key
            self._key = "".join([self._table[char] for char in sorted(self._table.keys())])
            self._language = language if language is not None else define_language("".join(self._table.values()))
        else:
            raise ValueError("Key should be str or dict[str, str]")
        if not self.is_valid():
            raise ValueError("Key should contain all unic letters from language.")

    def is_valid(self) -> bool:
        unic = {}
        for letter in self._table.values():
            if letter not in unic:
                unic[letter] = 1
            else:
                return False
        return any(char.isalpha() and (char.lower() in self._language.abc) for char in self._table.values())

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        return self._table.keys().__iter__()

    def __str__(self) -> str:
        return self._key

    def __getitem__(self, item):
        return self._table[item]

    @property
    def language(self) -> Language:
        return self._language

    @property
    def table(self) -> dict:
        return self._table

    def reversed(self):
        """Returns reversed key."""
        reversed_table = {v: k for k, v in self._table.items()}
        return TableKey(reversed_table, language=self._language)

    def swap_decrypted_letters(self, swap: tuple[str, str]):
        """Swaps decrypted letters in key."""
        decrypted_letter_1, decrypted_letter_2 = swap
        self.table[decrypted_letter_1], self.table[decrypted_letter_2] = self.table[decrypted_letter_2], self.table[
            decrypted_letter_1]

    def __copy__(self):
        return TableKey(copy(self._table), language=self._language)
