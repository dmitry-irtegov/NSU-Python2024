import unittest

output = []
def mock_print(num, **kwargs):
    if isinstance(num, int):
        output.append(num)

orig_print = print
print = mock_print
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

    def test(self):
        collatz(50)
        self.assertEqual(output, [50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        with self.assertRaises(ValueError):
            collatz(0)
        with self.assertRaises(ValueError):
            collatz(-1)



