import argparse
import bisect
from pathlib import Path


def directory_type(path: str) -> Path:
    casted = Path(path)

    if not casted.exists():
        message = f"not exists: {casted}"
        raise argparse.ArgumentTypeError(message)

    if not casted.is_dir():
        message = f"not a directory: {casted}"
        raise argparse.ArgumentTypeError(message)

    return casted


def key(item: tuple[int, str]) -> tuple[int, str]:
    return -item[0], item[1]


def main() -> None:
    parser = argparse.ArgumentParser(
        "file-ls",
        description="List all files in the given directory."
    )
    parser.add_argument(
        "directory", type=directory_type,
        help="a target dictionary",
    )


    items: list[tuple[int, str]] = []
    directory: Path = parser.parse_args().directory
    for entry in directory.iterdir():
        if entry.is_file():
            item = entry.lstat().st_size, entry.name
            bisect.insort(items, item, key=key)

    print("\n".join(f"{size}\t\t{name}" for (size, name) in items))


if __name__ == "__main__":
    main()
