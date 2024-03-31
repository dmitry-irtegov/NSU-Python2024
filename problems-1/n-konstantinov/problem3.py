from unittest import TestCase


def collatz_conjecture(num):
    yield num
    while num != 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        yield num


def collatz_conjecture_list(num):
    return list(collatz_conjecture(num))


def format_collatz_list(collatz_list):
    return '->'.join(str(num) for num in collatz_list)


class TestProblem(TestCase):
    def test_default(self):
        expected_list = [3, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(expected_list, collatz_conjecture_list(3))

    def test_formatted_output(self):
        collatz_list = collatz_conjecture_list(3)
        expected_string = "3->10->5->16->8->4->2->1"
        self.assertEqual(expected_string, format_collatz_list(collatz_list))

    def test_one(self):
        expected_list = [1]
        self.assertEqual(expected_list, collatz_conjecture_list(1))

    def test_even_number(self):
        expected_list = [6, 3, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(expected_list, collatz_conjecture_list(6))

    def test_odd_number(self):
        expected_list = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        self.assertEqual(expected_list, collatz_conjecture_list(7))

    def test_large_number(self):
        collatz_list = collatz_conjecture_list(1000000)
        self.assertEqual(1, collatz_list[-1])
