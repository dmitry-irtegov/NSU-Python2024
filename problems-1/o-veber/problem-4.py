from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO


def print_song_text():
    bottle_count = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'no']
    bottle_fall = '{} one green bottle should accidentally fall{}'
    will_be = '{}{} green {} hanging on the wall{}'
    nothing = ''
    comma = ','
    for i in range(10):
        condition = "And if" if i != 9 else "If that"
        counts = "bottles" if i != 9 else "bottle"
        comma_or_nothing = ',' if i != 9 else ''
        will_be_counts = "bottles" if i != 8 else "bottle"
        print(will_be.format(nothing, bottle_count[i], counts, comma))
        print(will_be.format(nothing, bottle_count[i], counts, comma))
        print(bottle_fall.format(condition, comma_or_nothing))
        print(will_be.format('There\'ll be ', str.lower(bottle_count[i + 1]), will_be_counts, '.'))


class TestDictionary(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_green_bottles(self, stdout):
        print_song_text()
        self.assertEqual(stdout.getvalue(), """Ten green bottles hanging on the wall,
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
""")


if __name__ == '__main__':
    main()
