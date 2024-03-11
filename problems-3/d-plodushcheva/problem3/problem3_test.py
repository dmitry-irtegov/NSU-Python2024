import unittest
from problem3 import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector([1, 2, 3])
        self.v2 = Vector([4, 5, 6])

    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(str(result), "[5, 7, 9]")

    def test_sub(self):
        result = self.v1 - self.v2
        self.assertEqual(str(result), "[-3, -3, -3]")

    def test_scalar_mul(self):
        result = self.v1 * 2
        self.assertEqual(str(result), "[2, 4, 6]")

    def test_mult(self):
        self.v1.mult(self.v2)
        self.assertEqual(str(self.v1), "[4, 10, 18]")

    def test_dot(self):
        result = self.v1.dot(self.v2)
        self.assertEqual(result, 32)

    def test_compare(self):
        v3 = Vector([1, 2, 3])
        self.assertTrue(self.v1.compare(v3))

    def test_length(self):
        result = self.v1.length()
        self.assertEqual(result, 3.7416573867739413)

    def test_get(self):
        result = self.v1.get(1)
        self.assertEqual(result, 2)

    def test_str(self):
        result = str(self.v1)
        self.assertEqual(result, "[1, 2, 3]")


if __name__ == '__main__':
    unittest.main()
