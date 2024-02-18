import unittest

NUMBERS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
           7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
HANGING = "%s green bottle%s hanging on the wall,\n"
IF_STRING = "And if one green bottle should accidentally fall,\n"
IF_ONE_STRING = "If that one green bottle should accidentally fall\n"
ANY_BOTTLES = "There’ll be %s green bottle%s hanging on the wall.\n"
NO_BOTTLES = "There’ll be no green bottles hanging on the wall.\n"


def song_part(num):
    return (HANGING % (NUMBERS[num], "" if num == 1 else "s")
            + HANGING % (NUMBERS[num], "" if num == 1 else "s")
            + (IF_ONE_STRING if num == 1 else IF_STRING)
            + f'{NO_BOTTLES if num == 1 else ANY_BOTTLES % (NUMBERS[num - 1].lower(), "" if num - 1 == 1 else "s")}')


def sing_song():
    return "".join([song_part(bottles_num) for bottles_num in range(10, 0, -1)])


class TestSong(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sing_song(),
                         """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There’ll be no green bottles hanging on the wall.
""")


if __name__ == '__main__':
    unittest.main()
