import unittest


def limit(numbers: list[int], lower: int, upper: int) -> list[int]:
    return [ num if lower < num < upper else (lower if num <= lower else upper) for num in numbers ]


class TestLimit(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(limit([], 3, 6), [])

    def test_main(self):
        self.assertEqual(limit([x for x in range(10)], 3, 6), [3, 3, 3, 3, 4, 5, 6, 6, 6, 6])

    def test_non_inclusive(self):
        self.assertEqual(limit([4, 5, 4, 3, 5, 6], 1, 10), [4, 5, 4, 3, 5, 6])

    def test_split(self):
        self.assertEqual(limit([0, 1, 2, 15, 16, 17], 4, 6), [4, 4, 4, 6, 6, 6])

if __name__ == "__main__":
    unittest.main()
