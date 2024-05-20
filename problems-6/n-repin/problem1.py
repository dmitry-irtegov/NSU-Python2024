import unittest
import random

from typing import Callable

from random import sample

SAMPLE_TEXT = 'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus Pagemaker, в шаблонах которых используется Lorem Ipsum.'
SAMPLE_TEXT_SHORT = 'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне.'

def apply_words(text: str, callback: Callable[[str], str]) -> str:
    new_text = ''
    current_word = ''
    
    for letter in text:
        if letter.isalnum():
            current_word += letter
        else:
            if current_word != '':
                new_text += callback(current_word)
                current_word = ''

            new_text += letter            

    if current_word != '':
        new_text += callback(current_word)

    return new_text

def scramble_letters(text: str, seed=None) -> str:
    if len(text) <= 2:
        return text

    if seed is not None:
        random.seed(seed)

    substring = text[1:-1]
    
    substring = ''.join(sample(substring, len(substring)))
    
    text = text[0] + substring + text[-1]

    return text

def sort_letters(text: str):
    if len(text) <= 2:
        return text

    substring = text[1:-1]
    
    substring = ''.join(sorted(substring))
    
    text = text[0] + substring + text[-1]

    return text

class TestRewriter(unittest.TestCase):

    def test_empty(self):
        result = apply_words('', lambda x: x)

        self.assertEqual(result, '')

    def test_sample_scramble(self):
        TARGET_42_SEED = 'Leorm Iupsm - это тсект-"рыба", чтасо ипсьыузмолей в петчаи и вэб-диназйе.'

        result = apply_words(SAMPLE_TEXT_SHORT, lambda x: scramble_letters(x, seed=42))

        self.assertEqual(result, TARGET_42_SEED)

    def test_sample_sorted(self):
        TARGET_SORTED = 'Leorm Ipsum - это текст-"рбыа", часто иезлмопсуыьй в паетчи и вэб-дазийне.'

        result = apply_words(SAMPLE_TEXT_SHORT, sort_letters)

        self.assertEqual(result, TARGET_SORTED)


if __name__ == '__main__':
    unittest.main()
