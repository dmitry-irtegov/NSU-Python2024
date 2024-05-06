import unittest
from unittest.mock import patch

def findpos(sub):
    with open('pi.txt', 'r') as file:
        pi = ''.join(line.strip() for line in file)
    positions = []
    x = pi.find(sub)
    while x != -1:
        positions.append(x - 1)
        x = pi.find(sub, x + 1)
    count = len(positions)
    if count < 5:
        print(f"found {count} results.\npositions: {positions}\n")
    else:
        print(f"found {count} results.\npositions: {positions[:5]}\n")

class TestsFindPosition(unittest.TestCase):
    @patch('builtins.print')
    def test_qwerty(self, mock_print):
        findpos("123456")
        mock_print.assert_called_with("found 2 results.\npositions: [2458885, 3735793]\n")

    @patch('builtins.print')
    def test_five(self, mock_print):
        findpos("10049")
        mock_print.assert_called_with("found 49 results.\npositions: [81181, 81663, 164755, 166002, 227951]\n")

    @patch('builtins.print')
    def test_one(self, mock_print):
        findpos("1")
        mock_print.assert_called_with("found 419139 results.\npositions: [1, 3, 37, 40, 49]\n")

if __name__ == '__main__':
    unittest.main()
