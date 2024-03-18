import unittest
from problem3 import do_step, collatz_hypothesis


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
    unittest.main()
