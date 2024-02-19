from collections.abc import Iterator


def collatz_conjecture(start: int) -> Iterator[int]:
    yield start

    while start != 1:
        yield (start := (3 * start + 1 if start % 2 else start // 2))


def main() -> None:
    print(*collatz_conjecture(int(input())), sep=" -> ")


if __name__ == "__main__":
    main()
