import unittest


def collatz(num):
    if num <= 0:
        raise ValueError("number must be greater than 0")
    print(num, end="")
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        print(" -> ", end="")
        print(num, end="")


class CollatzFuncTest(unittest.TestCase):

    def setUp(self):
        global print
        self.output = []
        def mock_print(num, **kwargs):
            if isinstance(num, int):
                self.output.append(num)
        self.orig_print = print
        print = mock_print

    def tearDown(self):
        global print
        print = self.orig_print

    def test_even(self):
        collatz(50)
        self.assertEqual(self.output,
                         [50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26,
                          13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    def test_odd(self):
        collatz(21)
        self.assertEqual(self.output,
                         [21, 64, 32, 16, 8, 4, 2, 1])
    def errors_test(self):
        with self.assertRaises(ValueError):
            collatz(0)
        with self.assertRaises(ValueError):
            collatz(-1)


if '__main__' == __name__:
    unittest.main()
