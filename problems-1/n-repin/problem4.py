numbers_map: dict[int, str] = {
    0: "No",
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


first_line_format_string = "{current} green bottle{s} hanging on the wall,"
third_line_format_string = "{start} one green bottle should accidentally fall,"
last_line_format_string = "There’ll be {remaining} green bottle{s} hanging on the wall."


def format_ending(number: int) -> str:
    return "s" if number != 1 else ""


def format_first(number: int) -> str:
    current_word = numbers_map[number]

    ending = format_ending(number)

    return first_line_format_string.format(current=current_word, s=ending)


def format_third(last_verse: bool) -> str:
    if last_verse:
        return third_line_format_string.format(start="If that")
    else:
        return third_line_format_string.format(start="And if")


def format_last(number: int) -> str:
    remaining_word = numbers_map[number].lower()

    ending = format_ending(number)

    return last_line_format_string.format(remaining=remaining_word, s=ending)


def format_verse(current: int, remainig: int) -> str:
    return "\n".join([
        format_first(current),
        format_first(current),
        format_third(remainig == 0),
        format_last(remainig)
    ])


def format_song(verse_count: int):
    verses = [ format_verse(i, i - 1) for i in range(verse_count, 0, -1) ]

    return "\n\n".join(verses)


if __name__ == "__main__":
    print(format_song(10))
