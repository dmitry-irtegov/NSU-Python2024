import argparse
import enum
import random
import re
import sys


class Mode(enum.Enum):
    random = "random"
    ABC = "ABC"


MODE_MIXERS = {Mode.random: (lambda word_part: ''.join(random.sample(word_part, len(word_part)))),
               Mode.ABC: (lambda word_part: ''.join(sorted(list(word_part))))}


def init_parser():
    parser = argparse.ArgumentParser(description='Rearrange letters in words of a given text.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text', type=str, default="",
                       help='Input text')
    group.add_argument('--input', type=str, default="stdin",
                       help='Input file')

    parser.add_argument('--output', type=str, default="stdout",
                        help='Output file')
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

    if args.input == "stdin":
        result = replace_words(args.text, args.mode)
    else:
        try:
            result = ""
            for line in open(args.input, "r"):
                result += replace_words(line, args.mode)
        except Exception as e:
            sys.stderr.write(f"Failed while replacing words from file \"{args.input}\": {str(e)}")
            exit(1)

    if args.output == "stdout":
        print(result)
    else:
        try:
            with open(args.output, "w") as file:
                file.write(result)
        except Exception as e:
            sys.stderr.write(f"Failed while writing result to file \"{args.output}\": {str(e)}")
            exit(1)
