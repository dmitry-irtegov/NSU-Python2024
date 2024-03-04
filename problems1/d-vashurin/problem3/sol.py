from collections.abc import Iterator


def _collatz_iter(start: int) -> Iterator[int]:
    yield start

    while start != 1:
        yield (start := (3 * start + 1 if start % 2 else start // 2))


def collatz_conjecture(start: int) -> Iterator[int]:
    if start <= 0:
        message = "The Collatz conjecture is defined only for positive integers"
        raise ValueError(message)

    return _collatz_iter(start)


def main() -> None:
    print(*collatz_conjecture(int(input())), sep=" -> ")


if __name__ == "__main__":
    main()
