import json

from cipher.core.entity.language import Language
from cipher.table.entity.text import TableText
import cipher.settings as settings


def text_to_frequencies(text: TableText) -> dict[str, float]:
    frequencies = {letter: 0 for letter in text.language.abc}
    ngram_counts = 0

    for word in text.words:
        ngram_counts += len(word)
        for letter in word:
            if letter in frequencies:
                frequencies[letter] += 1
    if ngram_counts > 0:
        for letter in frequencies.keys():
            frequencies[letter] /= ngram_counts
        return frequencies
    else:
        raise ValueError("Text is empty")


def load_frequencies(language: Language) -> dict[str, float]:
    with open(settings.FREQUENCIES_PATH + f"{str(language.name)}.json") as file:
        frequencies = json.load(file)
        return frequencies
