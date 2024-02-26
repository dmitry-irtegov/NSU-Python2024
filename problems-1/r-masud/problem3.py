import unittest

def collatz_conjecture(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz_conjecture(n // 2)
    else:
        return [n] + collatz_conjecture(3 * n + 1)

class TestCollatzConjecture(unittest.TestCase):

    def test_multiple_inputs(self):
        test_cases = [
            (1, [1]),
            (10, [10, 5, 16, 8, 4, 2, 1]),
            (20, [20, 10, 5, 16, 8, 4, 2, 1]),
            (100, [100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        ]

        for number, expected_chain in test_cases:
            with self.subTest(number=number, expected_chain=expected_chain):
                self.assertEqual(collatz_conjecture(number), expected_chain)

    def test_small_input(self):
        self.assertEqual(collatz_conjecture(2), [2, 1])

    def test_large_input(self):
        self.assertEqual(collatz_conjecture(1000000),
                         [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 46876, 23438, 11719, 35158, 17579,
                          52738, 26369, 79108, 39554, 19777, 59332, 29666, 14833, 44500, 22250, 11125, 33376, 16688,
                          8344, 4172, 2086, 1043, 3130, 1565, 4696, 2348, 1174, 587, 1762, 881, 2644, 1322, 661, 1984,
                          992, 496, 248, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91,
                          274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593,
                          1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638,
                          319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734,
                          1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325,
                          976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2,
                          1])


if __name__ == '__main__':
    unittest.main()