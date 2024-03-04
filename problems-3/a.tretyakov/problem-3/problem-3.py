import math
import unittest


class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of components")
        new_components = [x + y for x, y in zip(self.components, other.components)]
        return Vector(*new_components)

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of components")
        new_components = [x - y for x, y in zip(self.components, other.components)]
        return Vector(*new_components)

    def __mul__(self, scalar):
        new_components = [x * scalar for x in self.components]
        return Vector(*new_components)

    def __pow__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of components")
        return sum(x * y for x, y in zip(self.components, other.components))

    def __eq__(self, other):
        return self.components == other.components

    def __getitem__(self, index):
        return self.components[index]

    def __len__(self):
        return len(self.components)

    def __str__(self):
        return f"Vector{self.components}"

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))


class TestVector(unittest.TestCase):

    def setUp(self) -> None:
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)

    def test_addition(self):
        result = self.v1 + self.v2
        self.assertEqual(result.components, (5, 7, 9))

    def test_subtraction(self):
        result = self.v2 - self.v1
        self.assertEqual(result.components, (3, 3, 3))

    def test_scalar_multiplication(self):
        result = self.v1 * 2
        self.assertEqual(result.components, (2, 4, 6))

    def test_dot_product(self):
        result = self.v1 ** self.v2
        self.assertEqual(result, 32)

    def test_equality(self):
        self.assertTrue(self.v1 == self.v1)

    def test_getitem(self):
        self.assertEqual(self.v1[1], 2)

    def test_magnitude(self):
        v1 = Vector(3, 4)
        self.assertAlmostEqual(v1.magnitude(), 5.0)

    def test_raises(self):
        v2 = Vector(1)
        self.assertRaises(ValueError, Vector.__add__, self.v1, v2)
        self.assertRaises(ValueError, Vector.__sub__, self.v1, v2)
        self.assertRaises(ValueError, Vector.__pow__, self.v1, v2)


if __name__ == '__main__':
    unittest.main()
