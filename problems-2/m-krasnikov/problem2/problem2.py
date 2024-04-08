import unittest


def invert_dictionary(filename):
    with (open(filename) as file):
        latin_to_eng_dict = dict()
        for line in file.readlines():
            eng_word, latin_words = line.split('-')
            eng_word = eng_word.strip()
            for latin_word in latin_words.split(','):
                latin_word = latin_word.strip()
                if latin_word not in latin_to_eng_dict:
                    latin_to_eng_dict[latin_word] = [eng_word]
                else:
                    latin_to_eng_dict[latin_word].append(eng_word)

    return {latin_word: sorted(latin_to_eng_dict[latin_word]) for latin_word in sorted(latin_to_eng_dict.keys())}


class TestDictionary(unittest.TestCase):

    def test_one_word(self):
        self.assertEqual(invert_dictionary('one_word_test.txt'), {
            "last_latin": ["test_eng_word"],
            "latin_word": ["test_eng_word"],
            "one_more_latin": ["test_eng_word"],
            "other_latin": ["test_eng_word"]
        })

    def test_several_words(self):
        self.assertEqual(invert_dictionary('several_words_test.txt'), {
            "baca": ["fruit"],
            "bacca": ["fruit"],
            "malum": ["apple", "punishment"],
            "multa": ["punishment"],
            "pomum": ["apple"],
            "popula": ["apple"],
            "popum": ["fruit"]
        })

    def test_many_words(self):
        print(invert_dictionary("many_words_test.txt"))
        self.assertEqual(invert_dictionary('many_words_test.txt'), {
            'latin1': ['eng1', 'eng2', 'eng4', 'eng6', 'eng7'],
            'latin2': ['eng1', 'eng3', 'eng4', 'eng5', 'eng6', 'eng7', 'eng8'],
            'latin3': ['eng1', 'eng2', 'eng4', 'eng5', 'eng7', 'eng8'],
            'latin4': ['eng1', 'eng2', 'eng3', 'eng4', 'eng5', 'eng6', 'eng8'],
            'latin5': ['eng1', 'eng2', 'eng3', 'eng4', 'eng6', 'eng7', 'eng8'],
            'latin6': ['eng1', 'eng3', 'eng8'],
            'latin7': ['eng3', 'eng5', 'eng8'],
            'latin8': ['eng2', 'eng4', 'eng5', 'eng6', 'eng7'],
            'latin9': ['eng2', 'eng3', 'eng5', 'eng6', 'eng7']
        })


if __name__ == "__main__":
    unittest.main()
