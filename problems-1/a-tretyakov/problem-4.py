numbers_dict = {
    10: "Ten",
    9: "Nine",
    8: "Eight",
    7: "Seven",
    6: "Six",
    5: "Five",
    4: "Four",
    3: "Three",
    2: "Two",
    1: "One",
    0: "No"
}


def ten_green_bottles_lyrics(count=10):
    if count == 0:
        return

    word_end = "" if count == 1 else "s"
    phrase_postfix = f"green bottle{word_end} hanging on the wall"

    for i in range(2):
        print(f"{numbers_dict[count]} {phrase_postfix},")

    print("And if one green bottle should accidentally fall,")
    print(f"There’ll be {numbers_dict[count - 1].lower()} {phrase_postfix}.")

    ten_green_bottles_lyrics(count - 1)


if __name__ == "__main__":
    ten_green_bottles_lyrics()
