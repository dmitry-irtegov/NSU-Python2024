import argparse
import enum
import random
import re
import sys
from io import TextIOWrapper


class Mode(enum.Enum):
    random = "random"
    ABC = "ABC"


MODE_MIXERS = {Mode.random: (lambda word_part: ''.join(random.sample(word_part, len(word_part)))),
               Mode.ABC: (lambda word_part: ''.join(sorted(list(word_part))))}


def init_parser():
    parser = argparse.ArgumentParser(description='Rearrange letters in words of a given text.')
    parser.add_argument('--input', type=argparse.FileType('r'), default=sys.stdin,
                        help='Input file (default: stdin)')

    parser.add_argument('--output', type=argparse.FileType('r'), default=sys.stdout,
                        help='Output file (default: stdout)')
    parser.add_argument('--mode', type=Mode, default=Mode.random,
                        help='"random" or "ABC" mode for words')
    return parser


def replace_words(text: str, mode: Mode) -> str:
    mixer = MODE_MIXERS.get(mode)
    result_text = text
    words = re.findall(r"[\w']+", text)
    for word in words:
        if len(word) > 2:
            new_word = word[0] + mixer(word[1:-1]) + word[-1]
        else:
            new_word = word
        result_text = result_text.replace(word, new_word, 1)
    return result_text


if __name__ == '__main__':
    args = init_parser().parse_args()
    try:
        result = ""
        for line in args.input:
            result += replace_words(line, args.mode)
    except Exception as e:
        sys.stderr.write(f"Failed while replacing words from file \"{args.input.name}\": {str(e)}")
        exit(1)

    try:
        args.output.write(result)
    except Exception as e:
        sys.stderr.write(f"Failed while writing result to file \"{args.output}\": {str(e)}")
        exit(1)
