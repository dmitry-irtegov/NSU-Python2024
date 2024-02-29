import unittest

def create_latin_english_dictionary(english_latin_dict):
    latin_english_dict = {}

    for english_word, latin_translations in english_latin_dict.items():
        for latin_word in latin_translations:
            latin_english_dict.setdefault(latin_word, []).append(english_word)

    return latin_english_dict

class TestCreateLatinEnglishDictionary(unittest.TestCase):
    def test_basic_conversion(self):
        english_latin_dict = {
            'apple': ['malum', 'pomum', 'popula'],
            'fruit': ['baca', 'bacca', 'popum'],
            'punishment': ['malum', 'multa']
        }

        latin_english_dict = create_latin_english_dictionary(english_latin_dict)

        self.assertEqual(latin_english_dict['malum'], ['apple', 'punishment'])
        self.assertEqual(latin_english_dict['pomum'], ['apple'])
        self.assertEqual(latin_english_dict['popula'], ['apple'])
        self.assertEqual(latin_english_dict['baca'], ['fruit'])
        self.assertEqual(latin_english_dict['bacca'], ['fruit'])
        self.assertEqual(latin_english_dict['popum'], ['fruit'])
        self.assertEqual(latin_english_dict['multa'], ['punishment'])

    def test_empty_input(self):
        empty_dict = {}
        self.assertEqual(create_latin_english_dictionary(empty_dict), {})

    def test_duplicate_words(self):
        english_latin_dict = {
            'apple': ['malum', 'pomum', 'popula'],
            'fruit': ['baca', 'bacca', 'popum'],
            'punishment': ['malum', 'multa'],
            'orange': ['malum']
        }

        latin_english_dict = create_latin_english_dictionary(english_latin_dict)

        self.assertEqual(latin_english_dict['malum'], ['apple', 'punishment', 'orange'])

if __name__ == '__main__':
    unittest.main()
