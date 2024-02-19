verse: str = """{current} green bottles hanging on the wall,
{current} green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be {remaining} green bottles hanging on the wall."""


last_verse: str = """One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There’ll be no green bottles hanging on the wall."""


numbers_map: dict[int, str] = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}


def format_verse(current: int, remainig: int) -> str:
    current_word = numbers_map[current]
    remaining_word = numbers_map[remainig].lower()

    return verse.format(current=current_word, remaining=remaining_word)


def format_song(verse_count: int):
    verses = []

    for i in range(verse_count, 1, -1):
        verses.append(format_verse(i, i - 1))

    verses.append(last_verse)

    return "\n\n".join(verses)


if __name__ == "__main__":
    print(format_song(10))
