import io
import unittest
from unittest import TestCase
from unittest.mock import patch


def bottles_lyrics():
    numbers_capitalized = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    numbers_lowercase = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def bottle_format(index):
        return "bottle" if index == 2 else "bottles"

    for i in range(10, 0, -1):
        if i == 1:
            print("One green bottle hanging on the wall,")
            print("One green bottle hanging on the wall,")
            print("If that one green bottle should accidentally fall")
            print("There'll be no green bottles hanging on the wall.")
        else:
            print(f"{numbers_capitalized[i - 2]} green bottles hanging on the wall,")
            print(f"{numbers_capitalized[i - 2]} green bottles hanging on the wall,")
            print("And if one green bottle should accidentally fall,")
            print(f"There'll be {numbers_lowercase[i - 2]} green {bottle_format(i)} hanging on the wall.")


class TestBottlesLyrics(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bottles_lyrics(self, mock_stdout):
        expected_output = '''Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
If that one green bottle should accidentally fall
There'll be no green bottles hanging on the wall.
'''
        bottles_lyrics()
        self.assertEqual(expected_output, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
