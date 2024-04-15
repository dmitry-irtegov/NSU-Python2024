#!/usr/bin/env python3
import argparse
import sys
import random

from itertools import dropwhile

class _WordsRearranger:
    def __init__(self, rearrange_func):
        self.__rearrange_func = rearrange_func
    

    def rearrange_word(self, s):
        beg = next(dropwhile(lambda i: not s[i].isalpha(), range(len(s))), len(s)) + 1
        end = next(dropwhile(lambda i: not s[i].isalpha(), reversed(range(beg, len(s)))), beg)

        if end - beg < 1:
            return s

        return s[:beg] +  self.__rearrange_func(s[beg:end]) + s[end:]


    def rearrange_text(self, text):
        return ' '.join(map(self.rearrange_word, text.split()))


class RandomizedWordsRearranger(_WordsRearranger):
    def __init__(self, seed = None):
        rand = random.Random(seed)
        def shuffle_func(s):
            return ''.join(rand.sample(list(s), k = len(s)))

        _WordsRearranger.__init__(self, shuffle_func)


class SortedWordsRearranger(_WordsRearranger):
    def __init__(self):
        def sort_func(s):
            return ''.join(sorted(s))

        _WordsRearranger.__init__(self, sort_func)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='textrearranger',
        description='Rearrange words in a text, by default shuffles them.')

    parser.add_argument('--sorted',
        help='Instead of shuffling words sort characters in them alphabetically',
        action=argparse.BooleanOptionalAction)

    parser.add_argument('--seed',
        help='Specify a seed for a shuffling with RNG',
        required = False,
        default = None,
        nargs='?',
        type=int)


    args = parser.parse_args()

    if args.sorted:
        rearranger = SortedWordsRearranger()
    else:
        rearranger = RandomizedWordsRearranger(args.seed)

    while True:
        try:   
            text = input()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
        except BaseException as e:
            print(f'\nMet {repr(e)} while reading from stdin. Exiting.', file=sys.stderr)
            sys.exit(1)

        print(rearranger.rearrange_text(text))
