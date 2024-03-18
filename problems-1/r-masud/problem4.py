

import unittest
def writing_verse(number: int) ->str:
    numbers = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
               6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

    bottle = "green bottle"
    hanging_on_the_wall = " hanging on the wall"

    text = ""

    number_word = numbers[number].capitalize()

    plural_s, condition = ("s", "And if") if number != 1 else ("", "If that")

    for _ in range(2):
        text += f"{number_word} {bottle}{plural_s}{hanging_on_the_wall},\n"

    text += f"{condition} one {bottle} should accidentally fall\n"

    next_number = numbers[number - 1]
    plural_s_next = "s" if number - 1 != 1 else ""

    text += f"There’ll be {next_number} {bottle}{plural_s_next}{hanging_on_the_wall}.\n"

    return text

def writing_song() -> str:
    song_text=""

    for i in range(10, 0, -1):
        song_text += writing_verse(i)

    return song_text

if __name__ == "__main__":
    print(writing_song())


# testing part

class TestSongFunctions(unittest.TestCase):
    def test_writing_verse(self):
        expected_output = ("Ten green bottles hanging on the wall,\n"
                           "Ten green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be nine green bottles hanging on the wall.\n")
        self.assertEqual(writing_verse(10), expected_output)

    def test_writing_song(self):
        expected_output = ("Ten green bottles hanging on the wall,\n"
                           "Ten green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be nine green bottles hanging on the wall.\n"
                           "Nine green bottles hanging on the wall,\n"
                           "Nine green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be eight green bottles hanging on the wall.\n"
                           "Eight green bottles hanging on the wall,\n"
                           "Eight green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be seven green bottles hanging on the wall.\n"
                           "Seven green bottles hanging on the wall,\n"
                           "Seven green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be six green bottles hanging on the wall.\n"
                           "Six green bottles hanging on the wall,\n"
                           "Six green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be five green bottles hanging on the wall.\n"
                           "Five green bottles hanging on the wall,\n"
                           "Five green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be four green bottles hanging on the wall.\n"
                           "Four green bottles hanging on the wall,\n"
                           "Four green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be three green bottles hanging on the wall.\n"
                           "Three green bottles hanging on the wall,\n"
                           "Three green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be two green bottles hanging on the wall.\n"
                           "Two green bottles hanging on the wall,\n"
                           "Two green bottles hanging on the wall,\n"
                           "And if one green bottle should accidentally fall\n"
                           "There’ll be one green bottle hanging on the wall.\n"
                           "One green bottle hanging on the wall,\n"
                           "One green bottle hanging on the wall,\n"
                           "If that one green bottle should accidentally fall\n"
                           "There’ll be no green bottles hanging on the wall.\n"
                           )
        actual_output = writing_song()
        expected_output = expected_output.replace(" And", "And")

        self.assertEqual(actual_output, expected_output)