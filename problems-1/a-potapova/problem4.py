NUMBERS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
           9: "nine",
           10: "ten"}
BOTTLE = "green bottle"
HANDING_ON_THE_WALL = " hanging on the wall"


def make_verse(i: int):
    text = ""
    number = NUMBERS[i].capitalize()
    s, and_if = ("s", "And if") if i != 1 else ("", "If that")
    for _ in range(2):
        text = text + f"{number} {BOTTLE}{s}{HANDING_ON_THE_WALL},\n"

    text = text + f"{and_if} one {BOTTLE} should accidentally fall\n"
    number = NUMBERS[i - 1]
    s = "s" if i - 1 != 1 else ""
    text = text + f"There’ll be {number} {BOTTLE}{s}{HANDING_ON_THE_WALL}.\n"
    return text


def make_song():
    text = ""
    for i in range(10, 0, -1):
        text = text + make_verse(i)
    return text


if __name__ == "__main__":
    print(make_song())