import argparse
import random
from collections.abc import Callable
from enum import StrEnum
from io import StringIO


def shuffle(word: str) -> str:
    if len(word) <= 2:
        return word

    middle = list(word[1: -1])
    random.shuffle(middle)

    return word[0] + "".join(middle) + word[-1]


def sort_alphabetically(word: str) -> str:
    if len(word) <= 2:
        return word

    return word[0] + "".join(sorted(word[1: -1].lower())) + word[-1]


def replace_algorithm(text: str, action: Callable[[str], str]) -> str:
    buffer = StringIO()
    index = 0

    other_start = 0
    word_start = None

    while index < len(text):
        while index < len(text) and not text[index].isalpha():
            index += 1

        buffer.write(text[other_start: index])

        word_start = index
        while index < len(text) and text[index].isalpha():
            index += 1

        buffer.write(action(text[word_start: index]))
        other_start = index


    replaced: str = buffer.getvalue()
    if len(replaced) < len(text):
        replaced += text[other_start:]

    return replaced


class ReplaceStrategy(StrEnum):
    RANDOM = "random"
    ALPHABETICALLY = "alphabet"

    @property
    def method(self) -> Callable[[str], str]:
        match self:
            case ReplaceStrategy.RANDOM:
                return shuffle
            case ReplaceStrategy.ALPHABETICALLY:
                return sort_alphabetically


def main() -> None:
    parser = argparse.ArgumentParser(
        "middle-replacer",
        description="Change positions of the middle letters in the words of the given text."
    )
    parser.add_argument(
        "-s", "--strategy", default=ReplaceStrategy.RANDOM,
        type=ReplaceStrategy, choices=ReplaceStrategy,
        help="action, which will be used to replace the letters",
    )
    parser.add_argument("text", type=str, help="the target text")

    args = parser.parse_args()
    print(replace_algorithm(args.text, args.strategy.method))


if __name__ == "__main__":
    main()
