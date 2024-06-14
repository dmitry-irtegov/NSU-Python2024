from argparse import ArgumentParser
from collections.abc import Collection, Mapping
from pathlib import Path
from sys import stderr
from typing import IO, NoReturn


def fail(message: str) -> NoReturn:
    print("error:", message, file=stderr)
    exit(1)


def provide_parser() -> ArgumentParser:
    parser = ArgumentParser(
        "thesaurus-reverse",
        description="Reverse the given thesaurus."
    )

    parser.add_argument(
        "input",
        type=Path,
        help="a file with a thesaurus for reversing",
    )

    parser.add_argument(
        "-o", "--output",
        default="reversed.txt",
        type=Path,
        help="the file where the reversed thesaurus will be stored",
    )

    return parser


def read_thesaurus(io: IO[str]) -> dict[str, list[str]]:
    line_idx = 0
    thesaurus: dict[str, list[str]] = {}
    while (line := io.readline()):
        line_idx += 1
        translation, sep, words = line.partition("-")
        if not sep:
            message = f"line {line_idx} is malformed: {line}"
            raise ValueError(message)

        thesaurus[translation.strip()] = [word.strip() for word in words.split(",")]

    return thesaurus


def reverse(thesaurus: Mapping[str, Collection[str]]) -> dict[str, list[str]]:
    r_thesaurus: dict[str, list[str]] = {}
    for word, translations in thesaurus.items():
        for translation in translations:
            r_translations = r_thesaurus.get(translation, [])
            r_translations.append(word)
            r_thesaurus[translation] = r_translations

    for r_translations in r_thesaurus.values():
        r_translations.sort()

    return r_thesaurus


def write_thesaurus(io: IO[str], thesaurus: Mapping[str, Collection[str]]) -> None:
    for word in sorted(thesaurus):
        io.write(word)
        io.write(" - ")
        io.write(", ".join(thesaurus[word]))
        io.write("\n")


def main() -> None:
    args = provide_parser().parse_args()

    try:
        thesaurus_file = open(args.input, "r")
    except OSError as exc:
        fail(f"failed to open the thesaurus file, reason - {exc.strerror}")

    try:
        with thesaurus_file:
            thesaurus = read_thesaurus(thesaurus_file)
    except ValueError as exc:
        fail(f"failed to read the thesaurus file, reason - {exc}")

    try:
        reversed_file = open(args.output, "w")
    except OSError as exc:
        fail(f"failed to open the output file, reason - {exc.strerror}")

    try:
        with reversed_file:
            write_thesaurus(reversed_file, reverse(thesaurus))
    except OSError as exc:
        fail(f"failed to save the reversed thesaurus, reason - {exc.strerror}")


if __name__ == "__main__":
    main()
