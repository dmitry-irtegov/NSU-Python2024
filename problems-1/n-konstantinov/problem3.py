from unittest import TestCase


def collatz_conjecture_step(num):
    if num % 2 == 0:
        return num // 2
    if num % 2 != 0:
        return num * 3 + 1


def collatz_conjecture(num):
    collatz_string = '' + str(num) + '->'
    cur_num = num
    while cur_num != 1:
        cur_num = collatz_conjecture_step(cur_num)
        collatz_string += str(cur_num)
        if cur_num != 1:
            collatz_string += '->'
    return collatz_string


class TestProblem(TestCase):
    def test_default(self):
        expected_string = "3->10->5->16->8->4->2->1"
        self.assertEqual(expected_string, collatz_conjecture(3))
