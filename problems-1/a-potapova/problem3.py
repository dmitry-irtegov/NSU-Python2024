import unittest


def do_step(number: int) -> int:
    return number // 2 if number % 2 == 0 else 3 * number + 1


def collatz_hypothesis(number: int):
    result = []
    current_number = number
    while current_number != 1:
        current_number = do_step(current_number)
        result.append(current_number)
    return result


class TestCollatzHypothesis(unittest.TestCase):

    def test_step(self):
        self.assertEqual(do_step(2), 1)
        self.assertEqual(do_step(4), 2)
        self.assertEqual(do_step(5), 16)

    def test_collatz_hypothesis(self):
        self.assertEqual(collatz_hypothesis(1), [])
        self.assertEqual(collatz_hypothesis(2), [1])
        self.assertEqual(collatz_hypothesis(4), [2, 1])
        self.assertEqual(collatz_hypothesis(5), [16, 8, 4, 2, 1])


if '__main__' == __name__:
    # unittest.main()

    input_number = int(input("Введите число: "))
    sequence = collatz_hypothesis(input_number)
    print(input_number, end="")
    for num in sequence:
        print(f" -> {num}", end="")
