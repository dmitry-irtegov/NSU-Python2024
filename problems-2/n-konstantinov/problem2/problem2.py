from unittest import TestCase


def convert_dictionary(input_file, output_file):
    with open(input_file, 'r') as file:
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

    sorted_latin_words = sorted(latin_english_dict.keys())

    with open(output_file, 'w') as file:
        for latin_word in sorted_latin_words:
            english_words = latin_english_dict[latin_word]
            file.write(f"{latin_word} - {', '.join(english_words)}\n")


convert_dictionary("test_input.txt", "test_output.txt")


class TestDictionaryConversion(TestCase):
    def test_dictionary_conversion(self):
        convert_dictionary("test_input.txt", "test_output.txt")

        with open("test_output.txt", 'r') as output_file, open("test_default_checker.txt", 'r') as checker_file:
            output_lines = output_file.readlines()
            checker_lines = checker_file.readlines()

        self.assertEqual(output_lines, checker_lines)
