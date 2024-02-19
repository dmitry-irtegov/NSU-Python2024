from re import search
from unittest import TestCase, main


def get_dictionary_from_file(filename='extended-dictionary.txt'):
    with (open(filename) as file):
        my_dictionary = dict()
        for line in file.readlines():
            word_to_translation = search(r'[A-Za-z]+\s*-(\s*\s*[A-Za-z]+\s*,?\s)+', line)
            if word_to_translation is None:
                continue
            word, translations = line.split('-')
            word = word.strip()
            for translation in translations.split(','):
                translation = translation.strip()
                if translation not in my_dictionary:
                    my_dictionary[translation] = set()
                my_dictionary[translation].add(word)
    for key in my_dictionary:
        my_dictionary[key] = sorted(my_dictionary[key])
    return my_dictionary


class TestDictionary(TestCase):
    def test_empty_dictionary(self):
        self.assertEqual({}, get_dictionary_from_file("empty-dictionary.txt"))

    def test_one_word_dictionary(self):
        self.assertEqual({'malum': ['punishment'], 'multa': ['punishment']},
                         get_dictionary_from_file('one-word-dictionary.txt'))

    def test_base_dictionary(self):
        self.assertEqual({'baca': ['fruit'],
                          'bacca': ['fruit'],
                          'inferior': ['inferior', 'lower'],
                          'interior': ['inner', 'interior'],
                          'malum': ['apple', 'punishment'],
                          'multa': ['punishment'],
                          'parvus': ['small', 'subtle'],
                          'pomum': ['apple'],
                          'popula': ['apple'],
                          'popum': ['fruit']}, get_dictionary_from_file('extended-dictionary.txt'))

    def test_junk_dictionary(self):
        self.assertEqual({}, get_dictionary_from_file('junk-dictionary.txt'))


if __name__ == "__main__":
    main()
