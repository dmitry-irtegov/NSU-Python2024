import unittest

def findpos(sub):
    with open('pi.txt', 'r') as file:
        pi = ''.join(line.strip() for line in file)
    positions = []
    x = pi.find(sub)
    while x != -1:
        positions.append(x - 1)
        x = pi.find(sub, x + 1)
    count = len(positions)
    print(f"found {count} results.\n")
    if count < 5:
        print(f"positions: {positions}\n")
    else:
        print(f"positions: {positions[:5]}\n")

class TestsFindPosition(unittest.TestCase):
    def setUp(self):
        global print
        self.orig_print = print
        print = self.myprint
        self.result = ''

    def tearDown(self):
        global print
        print = self.orig_print

    def myprint(self, x, **kwargs):
        if isinstance(x, str):
            self.result += x

    def test_qwerty(self):
        findpos("123456")
        self.assertEqual(self.result, "found 2 results.\npositions: [2458885, 3735793]\n")

    def test_five(self):
        findpos("10049")
        self.assertEqual(self.result, "found 49 results.\npositions: [81181, 81663, 164755, 166002, 227951]\n")

    def test_one(self):
        findpos("1")
        self.assertEqual(self.result, "found 419139 results.\npositions: [1, 3, 37, 40, 49]\n")

if __name__ == '__main__':
    unittest.main()
