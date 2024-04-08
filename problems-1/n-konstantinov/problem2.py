from unittest import TestCase


def sequence_cut(sequence, border_a, border_b):
    if border_a > border_b:
        raise ValueError("border_a must be lower then border_b")
    for index in range(len(sequence)):
        if sequence[index] < border_a:
            sequence[index] = border_a
        elif sequence[index] > border_b:
            sequence[index] = border_b
    return sequence


class TestProblem(TestCase):
    def test_default(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual( [3, 3, 3, 4, 5, 6, 7, 8, 8, 8], sequence_cut(sequence, 3, 8))

    def test_empty(self):
        sequence = []
        self.assertEqual([], sequence_cut(sequence, 3, 8))

    def test_borders_bad(self):
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with self.assertRaises(ValueError):
            sequence_cut(sequence, 8, 3)
