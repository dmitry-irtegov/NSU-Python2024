import argparse
import random
from io import StringIO


def shuffle(text: str) -> str:
    mutable = list(text)
    random.shuffle(mutable)
    return "".join(mutable)


def sort_alphabetically(text: str) -> str:
    return "".join(sorted(text.lower()))


def main() -> None:
    parser = argparse.ArgumentParser(
        "shuffler",
        description="Shuffle the middle letters in the words of the given text."
    )
    parser.add_argument(
        "-a", "--alphabet", action="store_true",
        help="sort the letters alphabetically instead of shuffling them"
    )
    parser.add_argument("text", type=str, help="the target text")

    args = parser.parse_args()
    action = sort_alphabetically if args.alphabet else shuffle

    text: str = args.text
    text_length = len(text)
    buffer = StringIO()
    i = 0
    j = 0

    while i < text_length:
        if not text[i].isalpha():
            i += 1
            continue

        buffer.write(text[j: i + 1])
        j = i
        i += 1
        while i < text_length and text[i].isalpha():
            i += 1

        buffer.write(action(text[j + 1: i - 1]))
        j = i - 1

    shuffled = buffer.getvalue()
    if len(shuffled) < text_length:
        shuffled += text[j:]

    print(shuffled)


if __name__ == "__main__":
    main()
