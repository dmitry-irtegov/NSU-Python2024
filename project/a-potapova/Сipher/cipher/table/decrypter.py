from copy import copy

from spellchecker import SpellChecker

from cipher.settings import MIN_ACCURACY_FOR_SWAP
from cipher.table.cipher import TableCipher
from cipher.core.decrypter import Decrypter
import cipher.table.entity.frequencydata as frequency
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText


def build_cipher_key(plain_freq: dict, cipher_freq: dict):
    """Build key by plain and cipher frequencies of letters."""
    sorted_plain_freq = sorted(plain_freq.items(), key=lambda x: x[1], reverse=True)
    sorted_cipher_freq = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)

    initial_key = {}
    for (plain_char, _), (cipher_char, _) in zip(sorted_plain_freq, sorted_cipher_freq):
        initial_key[plain_char] = cipher_char

    return initial_key


def word_accuracy(word: str, spell: SpellChecker) -> (float, list):
    """Calculates word accuracy and returns tuple of value and list of swaps"""
    predicted_word = spell.correction(word)
    if predicted_word is None:
        return 0, []
    if predicted_word == word:
        return 1, []
    if len(predicted_word) == len(word):
        bad_letters = [(letter_1, letter_2) for letter_1, letter_2 in zip(word, predicted_word) if letter_1 != letter_2]
        return (len(word) - len(bad_letters)) / len(word), bad_letters
    else:
        return 0, []


def text_accuracy(text: TableText, spell) -> float:
    """Return value for estimating accuracy of swap"""
    words_accuracy = [(word.lower(), word_accuracy(word.lower(), spell)) for word in text.words]
    return sum([accur for _, (accur, _) in words_accuracy]) / len(words_accuracy)


class FrequencyDecrypter(Decrypter):
    class SwapData:
        """Data about swap. For analyze key accuracy"""
        def __init__(self, key: TableKey, decrypted_text: TableText, accuracy: float):
            self._key: TableKey = key
            self._text: TableText = decrypted_text
            self._accuracy: float = accuracy

        @property
        def key(self) -> TableKey:
            return self._key

        @property
        def text(self) -> TableText:
            return self._text

        @property
        def accuracy(self) -> float:
            return self._accuracy

    @staticmethod
    def decode(text: TableText) -> (TableText, TableKey):
        """Decode text without key by frequencies of letters and spellchecker"""
        plain_freq = frequency.load_frequencies(text.language)
        text_freq = frequency.text_to_frequencies(text)
        key_table = build_cipher_key(plain_freq, text_freq)
        key = TableKey(key_table, language=text.language)

        decrypted_text = TableCipher.decrypt(text, key=key)
        spell = SpellChecker(language=text.language.name)
        accuracy = text_accuracy(decrypted_text, spell)
        print(decrypted_text)
        swap_data = FrequencyDecrypter.SwapData(copy(key), decrypted_text, accuracy)

        for _ in range(2):
            for k_word in range(len(text.words)):
                curr_word = swap_data.text.words[k_word]
                accuracy, wrong_letters = word_accuracy(curr_word.lower(), spell)
                if MIN_ACCURACY_FOR_SWAP < accuracy < 1:
                    for swap in wrong_letters:
                        key = copy(swap_data.key)
                        key.swap_decrypted_letters(swap)
                        decrypted_text = TableCipher.decrypt(text, key=key)
                        accuracy = text_accuracy(decrypted_text, spell)
                        if accuracy < swap_data.accuracy:
                            # Rollback swap
                            break
                        else:
                            # Continue
                            swap_data = FrequencyDecrypter.SwapData(key, decrypted_text, accuracy)

        return decrypted_text, key
