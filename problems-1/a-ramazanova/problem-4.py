import unittest


def ten_green_bottles():
    result = """"""
    numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    s1 = 'green bottles hanging on the wall'
    s2 = 'one green bottle should accidentally fall'
    s3 = 'There’ll be'
    for i in range(10):
        result += f'{numbers[i]} {s1},\n'
        result += f'{numbers[i]} {s1},\n'
        if i < 9:
            result += f'And if {s2},\n'
            result += f'{s3} {numbers[i + 1].lower()} {s1}.\n'
        else:
            result += f'If that {s2}\n'
            result += f'{s3} no {s1}.'
    print(result)
    return result


class TestSong(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(ten_green_bottles(),
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
If that one green bottle should accidentally fall
There’ll be no green bottles hanging on the wall.""")


if __name__ == '__main__':
    unittest.main()
