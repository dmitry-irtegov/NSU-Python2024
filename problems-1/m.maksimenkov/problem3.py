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

    def mock_print(self, num, **kwargs):
        if isinstance(num, int):
            self.output.append(num)

    def mocked_collatz(self, num):
        global print
        self.output = []
        orig_print = print
        print = self.mock_print
        collatz(num)
        print = orig_print
        return self.output

    def test(self):
        self.assertEqual(self.mocked_collatz(50),
                         [50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26,
                          13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        with self.assertRaises(ValueError):
            collatz(0)
        with self.assertRaises(ValueError):
            collatz(-1)


if '__main__' == __name__:
    unittest.main()
