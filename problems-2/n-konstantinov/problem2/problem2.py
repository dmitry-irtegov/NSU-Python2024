import sys
from unittest import TestCase


def convert_dictionary(input_file):
    try:
        file = open(input_file, "r")
    except Exception as e:
        raise Exception(f"Error: {str(e)}.\nFailed to open file: {input_file}")

    with file:
        lines = file.readlines()

    latin_english_dict = {}

    for line in lines:
        english_word, latin_translations = line.strip().split(' - ')
        latin_words = latin_translations.split(', ')

        for latin_word in latin_words:
            if latin_word in latin_english_dict:
                latin_english_dict[latin_word].append(english_word)
            else:
                latin_english_dict[latin_word] = [english_word]

    return latin_english_dict


def sorted_dict(dictionary):
    return dict(sorted(dictionary.items()))


class TestDictionaryConversion(TestCase):
    def test_single_word(self):
        self.assertEqual(sorted_dict(convert_dictionary('single_word_test.txt')), {
            'latinword': ['englishword']
        })

    def test_simple(self):
        self.assertEqual(sorted_dict(convert_dictionary('simple_test.txt')), {
            'latinword1': ['englishword1', 'englishword2'],
            'latinword2': ['englishword1'],
            'latinword3': ['englishword2']
        })

    def test_empty_file(self):
        self.assertEqual(sorted_dict(convert_dictionary('empty_test.txt')), {})

    def test_long_dictionary(self):
        self.assertEqual(sorted_dict(convert_dictionary('long_dictionary_test.txt')), {
            'latin1': ['english1', 'english4', 'english7', 'english10', 'english13', 'english16', 'english19'],
            'latin2': ['english1', 'english2', 'english5', 'english8', 'english11', 'english14', 'english17', 'english20'],
            'latin3': ['english1', 'english3', 'english6', 'english9', 'english12', 'english15', 'english18'],
            'latin4': ['english2', 'english4', 'english7'],
            'latin5': ['english2', 'english3', 'english5', 'english10'],
            'latin6': ['english3', 'english6', 'english11'],
            'latin7': ['english4', 'english8', 'english13'],
            'latin8': ['english5', 'english9', 'english14'],
            'latin9': ['english6', 'english12'],
            'latin10': ['english7', 'english15'],
            'latin11': ['english8', 'english16'],
            'latin12': ['english9', 'english17'],
            'latin13': ['english10', 'english18'],
            'latin14': ['english11', 'english19'],
            'latin15': ['english12', 'english20'],
            'latin16': ['english13'],
            'latin17': ['english14'],
            'latin18': ['english15'],
            'latin19': ['english16'],
            'latin20': ['english17'],
            'latin21': ['english18'],
            'latin22': ['english19'],
            'latin23': ['english20']
        })
