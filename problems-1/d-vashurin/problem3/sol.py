from collections.abc import Iterator
from sys import stderr


def _collatz_iter(start: int) -> Iterator[int]:
    yield start

    while start != 1:
        yield (start := (3 * start + 1 if start % 2 else start // 2))


def collatz_conjecture(start: int) -> Iterator[int]:
    if start <= 0:
        message = "The Collatz conjecture is defined only for positive integers"
        raise ValueError(message)

    return _collatz_iter(start)


def main() -> int:
    try:
        line = input()
    except EOFError:
        return 0

    try:
        start = int(line)
    except ValueError:
        print(f"Failed to convert '{line}' to integer", file=stderr)
        return 1

    try:
        conj = collatz_conjecture(start)
    except ValueError as exc:
        print(f"{exc}, while '{start}' was passed", file=stderr)
        return 2

    print(*conj, sep=" -> ")
    return 0


if __name__ == "__main__":
    exit(main())
