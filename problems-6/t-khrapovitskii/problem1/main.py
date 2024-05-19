import random

from letter_shuffler import LetterShuffler

if __name__ == '__main__':
    with open('text.txt', 'r', encoding='utf-8') as original:
        with open('shuffled.txt', 'w', encoding='utf-8') as shuffle:
            shuffler1 = LetterShuffler(random.shuffle, shuffle)
            while True:
                char = original.read(1)
                if char == '':
                    break
                shuffler1.give_char(char)

        original.seek(0)
        with open('sorted.txt', 'w', encoding='utf-8') as sort:
            shuffler2 = LetterShuffler(lambda x: x.sort(), sort)
            while True:
                char = original.read(1)
                if char == '':
                    break
                shuffler2.give_char(char)
