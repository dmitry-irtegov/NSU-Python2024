import unittest

def latin_sort_key(latin_word):
    return latin_word.lower()


def create_latin_english_dictionary(english_latin_dict):
    latin_english_dict = {}


    for english_word, latin_words in english_latin_dict.items():
        for latin_word in latin_words:
            if latin_word in latin_english_dict:
                latin_english_dict[latin_word].add(english_word)
            else:
                latin_english_dict[latin_word] = {english_word}

    # for sorting the keys in the Latin-English dictionary alphabetically, ignoring case
    sorted_keys = sorted(latin_english_dict.keys(), key=lambda x: x.lower())
    sorted_latin_english_dict = {key: sorted(latin_english_dict[key]) for key in sorted_keys}

    return sorted_latin_english_dict






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

        # checking if new dictionary elements are sorted
        self.assertEqual(list(latin_english_dict.keys()), ['baca', 'bacca', 'malum', 'multa', 'pomum', 'popula', 'popum'])

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

        self.assertEqual(latin_english_dict['malum'], ['apple', 'orange', 'punishment'])

        # checking if new dictionary elements are sorted
        expected_keys = ['baca', 'bacca', 'malum', 'multa', 'pomum', 'popula', 'popum']
        self.assertEqual(list(latin_english_dict.keys()), expected_keys)


if __name__ == '__main__':
    unittest.main()
