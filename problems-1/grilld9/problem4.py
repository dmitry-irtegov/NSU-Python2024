import unittest


def sing_the_song():
    templ_wall = " green bottles hanging on the wall"
    templ_fall = "And if one green bottle should accidentally fall,\n"
    templ_will = "There’ll be "
    amounts = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "no"]
    result = ""
    for i in range(10):
        result += amounts[i].capitalize() + templ_wall + ",\n"
        result += amounts[i].capitalize() + templ_wall + ",\n"
        result += templ_fall
        result += templ_will + amounts[i + 1] + templ_wall + ".\n"
    return result

# print(sing_the_song())

class BottleSongTest(unittest.TestCase):

    def test(self):
        self.assertEqual(sing_the_song(),
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
There’ll be one green bottles hanging on the wall.
One green bottles hanging on the wall,
One green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be no green bottles hanging on the wall.
""")