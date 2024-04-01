import unittest


def collatz_conjecture(n):
    res = [n]
    print(n, end=" ")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res.append(n)
        print("->", n, end=" ")
    return res


class TestCutNumbers(unittest.TestCase):

    def test_number_1(self):
        self.assertEqual(collatz_conjecture(1), [1])

    def test_number_2(self):
        self.assertEqual(collatz_conjecture(2), [2, 1])

    def test_number_3(self):
        self.assertEqual(collatz_conjecture(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_number_9(self):
        self.assertEqual(collatz_conjecture(9), [9, 28, 14, 7, 22, 11, 34, 17,
                                                 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


if __name__ == '__main__':
    # num = int(input("Введите число: "))
    # collatz_conjecture(num)
    unittest.main()
