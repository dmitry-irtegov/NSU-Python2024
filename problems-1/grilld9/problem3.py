import unittest
def collatz(num):
    if num <= 0:
        raise ValueError("number must be greater than 0")
    res = [num]
    print(num, end="")
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        print(" -> {}".format(num), end="")
        res.append(num)
    return res

class CollatzFuncTest(unittest.TestCase):

    def test(self):
        self.assertEqual(collatz(1), [1])
        self.assertEqual(collatz(5), [5, 16, 8, 4, 2, 1])
        with self.assertRaises(ValueError):
            collatz(0)
        with self.assertRaises(ValueError):
            collatz(-1)



