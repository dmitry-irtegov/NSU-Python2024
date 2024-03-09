import argparse
from collections import defaultdict
from io import TextIOWrapper


def main() -> None:
    parser = argparse.ArgumentParser(
        "dictionary-reverse",
        description="Reverse the given dictionary."
    )
    parser.add_argument(
        "input", type=argparse.FileType("r"),
        help="a file with a dictionary for reversing",
    )
    parser.add_argument(
        "-o", "--output", default="reversed.txt", type=argparse.FileType("w"),
        help="the file where the reversed dictionary will be stored",
    )

    args = parser.parse_args()

    read_file: TextIOWrapper = args.input
    dictionary: dict[str, set[str]] = defaultdict(set)

    with read_file:
        while (line := read_file.readline()):
            translation, _, words = line.partition("-")
            translation = translation.strip()
            for word in words.split(","):
                dictionary[word.strip()].add(translation)

    write_file: TextIOWrapper = args.output
    with write_file:
        for word in sorted(dictionary):
            write_file.write(f"{word} - {', '.join(sorted(dictionary[word]))}\n")


if __name__ == "__main__":
    main()
