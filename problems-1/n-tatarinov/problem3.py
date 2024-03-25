import unittest

def collatz(number):
    if number < 1 or round(number) != number:
        raise ValueError("non-int or non-positive input")
    chain = [str(number)]
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number*3 + 1
        chain.append(str(number))
    return ' --> '.join(chain)

class TestCollatzHypothesis(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(collatz(3), '3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1')
    def test_another_simple(self):
        self.assertEqual(collatz(8), '8 --> 4 --> 2 --> 1')
    def test_short_chain(self):
        self.assertEqual(collatz(1), '1')
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            collatz(-3)
    def test_float_input(self):
        with self.assertRaises(ValueError):
            collatz(5.5)

if __name__ == '__main__':
    unittest.main()
