import unittest
from problem3 import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)

    def test_size(self):
        self.assertEqual(len(self.v1), 3)

    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(str(result), "[5, 7, 9]")

    def test_sub(self):
        result = self.v1 - self.v2
        self.assertEqual(str(result), "[-3, -3, -3]")

    def test_scalar_mul(self):
        result = self.v1 * 2
        self.assertEqual(str(result), "[2, 4, 6]")

    def test_dot(self):
        result = self.v1.dot(self.v2)
        self.assertEqual(result, 32)

    def test_compare(self):
        v3 = Vector(1, 2, 3)
        self.assertTrue(self.v1 == v3)

    def test_length(self):
        result = self.v1.length()
        self.assertEqual(result, 3.7416573867739413)

    def test_get(self):
        result = self.v1[1]
        self.assertEqual(result, 2)

    def test_str(self):
        result = str(self.v1)
        self.assertEqual(result, "[1, 2, 3]")

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            self.v1 + 1

    def test_sub_value_error(self):
        with self.assertRaises(ValueError):
            self.v1 - Vector(1, 2)


if __name__ == '__main__':
    unittest.main()
