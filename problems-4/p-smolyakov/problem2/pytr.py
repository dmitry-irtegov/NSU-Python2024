#!/usr/bin/env python3
import argparse
import sys

class WrongTranslatorParametersException(Exception):
    pass

class DifferentAlphabetLengthsException(WrongTranslatorParametersException):
    pass

class InvalidAlphabetException(WrongTranslatorParametersException):
    pass

class Translator():
    def __init__(self, tr_from_alphabet, tr_to_alphabet, tr_remove_alphabet = ''):
        if not (isinstance(tr_from_alphabet, str) and isinstance(tr_to_alphabet, str) and isinstance(tr_remove_alphabet, str)):
            raise TypeError('only strings are allowed')

        if len(tr_from_alphabet) != len(tr_to_alphabet):
            raise DifferentAlphabetLengthsException(f'len(tr_from_alphabet)={len(tr_from_alphabet)} '
                + f'is not equal to len(tr_to_alphabet)={len(tr_to_alphabet)}')

        self.translation_table = {}

        for tr_from, tr_to in zip(tr_from_alphabet, tr_to_alphabet):
            if self.translation_table.get(tr_from, None) is not None:
                raise InvalidAlphabetException(f'duplicates in tr_from_alphabet: {tr_from}')
            self.translation_table[tr_from] = tr_to

        for tr_remove in tr_remove_alphabet:
            if self.translation_table.get(tr_remove, None) == '':
                raise InvalidAlphabetException(f'duplicates in tr_remove_alphabet: {tr_remove}')
            self.translation_table[tr_remove] = ''


    def translate(self, source):
        if not isinstance(source, str):
            raise TypeError('only strings are allowed')
        return ''.join(list(map(lambda char: self.translation_table.get(char, char), [*source])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='pytr',
        description='Pytranslate pyor pydelete pycharacters')
    parser.add_argument('from_alphabet', 
        help='alphabet with symbols to translate',
        type=str)
    parser.add_argument('to_alphabet', 
        help='alphabet with symbols be translated to ',
        type=str)
    parser.add_argument('-d', '--delete',
        help='alphabet with symbols for removal',
        required = False,
        default = '',
        nargs='?',
        type=str)

    args = parser.parse_args()
    try:
        tr = Translator(args.from_alphabet, args.to_alphabet, args.delete)
    except Exception as e:
        print(repr(e), file=sys.stderr)
        sys.exit(1)

    while True:
        try:   
            source = input()
        except (EOFError, KeyboardInterrupt):
            sys.exit(0)
        except BaseException as e:
            print(f'\nMet {repr(e)} while reading from stdin. Exiting.', file=sys.stderr)
            sys.exit(1)

        print(tr.translate(source))
