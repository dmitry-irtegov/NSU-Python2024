import unittest
import unittest
from problem4 import make_verse, make_song


class TestSong(unittest.TestCase):
    def test_print_verse(self):
        verse_1 = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be nine green bottles hanging on the wall.
"""
        self.assertEqual(make_verse(10), verse_1)
        verse_2 = """One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There’ll be no green bottles hanging on the wall.
"""
        self.assertEqual(make_verse(1), verse_2)

    def test_print_song(self):
        song = """Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall
There’ll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There’ll be no green bottles hanging on the wall.
"""
        self.assertEqual(make_song(), song)


if __name__ == "__main__":
    unittest.main()
