#!/usr/bin/env python3
import argparse
import sys
import random


class _WordsRearranger:
    def __init__(self, rearrange_func):
        self.__rearrange_func = rearrange_func
    

    def rearrange_word(self, s):
        if len(s) < 3:
            return s
        return self.__rearrange_func(s)


    def rearrange_text(self, text):
        return ' '.join(map(self.rearrange_word, text.split()))


class RandomizedWordsRearranger(_WordsRearranger):
    def __init__(self, seed = None):
        rand = random.Random(seed)
        def shuffle_func(s):
            return s[0] + ''.join(rand.sample(list(s[1:-1]), k = len(s) - 2)) + s[-1]

        _WordsRearranger.__init__(self, shuffle_func)


class SortedWordsRearranger(_WordsRearranger):
    def __init__(self):
        def sort_func(s):
            return s[0] + ''.join(sorted(s[1:-1])) + s[-1]

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
