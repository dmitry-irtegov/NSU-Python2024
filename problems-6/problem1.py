import random
import unittest


def shuffle_word(word):
    if len(word) <= 3:
        return word
    else:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]


def sort_word(word):
    if len(word) <= 3:
        return word
    else:
        middle = list(word[1:-1])
        middle.sort()
        return word[0] + ''.join(middle) + word[-1]


def process_text(text, word_processor):
    words = text.split()
    processed_words = []
    for word in words:
        alphanumeric_word = ''.join(char for char in word if char.isalpha())
        if alphanumeric_word:
            processed_word = word_processor(alphanumeric_word)
            word = ''.join(processed_word[j] if char.isalpha() else char for j, char in enumerate(word))
        processed_words.append(word)
    return ' '.join(processed_words)


class TestTextProcessing(unittest.TestCase):
    def setUp(self):
        self.seed = 42
        random.seed(self.seed)

    def test_shuffle_word(self):
        word = "example"
        shuffled_word = shuffle_word(word)
        self.assertEqual(len(word), len(shuffled_word))
        self.assertEqual(word[0], shuffled_word[0])
        self.assertEqual(word[-1], shuffled_word[-1])
        self.assertEqual("epamlxe", shuffled_word)

    def test_sort_word(self):
        word = "example"
        sorted_word = sort_word(word)
        self.assertEqual(len(word), len(sorted_word))
        self.assertEqual(word[0], sorted_word[0])
        self.assertEqual(word[-1], sorted_word[-1])
        self.assertEqual('ealmpxe', sorted_word)

    def test_process_text_shuffle(self):
        text = "Hello! This is an example text for testing."
        shuffled_text = process_text(text, shuffle_word)
        self.assertNotEqual(text, shuffled_text)
        self.assertEqual(len(text.split()), len(shuffled_text.split()))
        self.assertEqual("Hlelo! Tihs is an eplxame txet for tisteng.", shuffled_text)

    def test_process_text_sort(self):
        text = "Hello! This is an example text for testing."
        sorted_text = process_text(text, sort_word)
        self.assertNotEqual(text, sorted_text)
        self.assertEqual(len(text.split()), len(sorted_text.split()))
        self.assertEqual("Hello! This is an ealmpxe text for teinstg.", sorted_text)
