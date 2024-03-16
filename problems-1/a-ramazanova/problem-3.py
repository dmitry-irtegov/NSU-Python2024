import sys
import unittest
from io import StringIO


def collatz(n):
    result = [n]
    print(f"{n:.0f} ", end="")
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        print(f"-> {n:.0f} ", end="")
    return result


class TestCollatz(unittest.TestCase):
    def setUp(self):
        self.temp_stdout = StringIO()
        sys.stdout = self.temp_stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_collatz_sequence_3(self):
        collatz(3)
        expected_sequence = "3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 "
        actual_sequence = self.temp_stdout.getvalue()
        self.assertEqual(actual_sequence, expected_sequence)

    def test_collatz_sequence_20(self):
        collatz(20)
        expected_sequence = "20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 "
        actual_sequence = self.temp_stdout.getvalue()
        self.assertEqual(actual_sequence, expected_sequence)

    def test_collatz_sequence_27(self):
        collatz(27)
        expected_sequence = "27 -> 82 -> 41 -> 124 -> 62 -> 31 -> 94 -> 47 -> 142 -> 71 -> 214 -> 107 -> 322 -> 161 " \
                            "-> 484 -> 242 -> 121 -> 364 -> 182 -> 91 -> 274 -> 137 -> 412 -> 206 -> 103 -> 310 -> " \
                            "155 -> 466 -> 233 -> 700 -> 350 -> 175 -> 526 -> 263 -> 790 -> 395 -> 1186 -> 593 -> " \
                            "1780 -> 890 -> 445 -> 1336 -> 668 -> 334 -> 167 -> 502 -> 251 -> 754 -> 377 -> 1132 -> " \
                            "566 -> 283 -> 850 -> 425 -> 1276 -> 638 -> 319 -> 958 -> 479 -> 1438 -> 719 -> 2158 -> " \
                            "1079 -> 3238 -> 1619 -> 4858 -> 2429 -> 7288 -> 3644 -> 1822 -> 911 -> 2734 -> 1367 -> " \
                            "4102 -> 2051 -> 6154 -> 3077 -> 9232 -> 4616 -> 2308 -> 1154 -> 577 -> 1732 -> 866 -> " \
                            "433 -> 1300 -> 650 -> 325 -> 976 -> 488 -> 244 -> 122 -> 61 -> 184 -> 92 -> 46 -> 23 -> " \
                            "70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 "
        actual_sequence = self.temp_stdout.getvalue()
        self.assertEqual(actual_sequence, expected_sequence)

    def test_collatz_sequence_1(self):
        collatz(1)
        expected_sequence = "1 "
        actual_sequence = self.temp_stdout.getvalue()
        self.assertEqual(actual_sequence, expected_sequence)


if __name__ == '__main__':
    unittest.main()
