import math
import unittest


class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimensions to add")
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimensions to subtract")
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, scalar):
        return Vector(*(x * scalar for x in self.components))

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(x / scalar for x in self.components))

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of same dimensions for dot product")
        return sum(x * y for x, y in zip(self.components, other.components))

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalized(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self / mag

    def __eq__(self, other):
        return self.components == other.components

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        components = list(self.components)
        components[index] = value
        self.components = tuple(components)


class TestVector(unittest.TestCase):

    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)
        self.v3 = Vector(1, 2)
        self.zero_vector = Vector(0, 0, 0)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector(5, 7, 9))
        with self.assertRaises(ValueError):
            self.v1 + self.v3

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vector(-3, -3, -3))
        with self.assertRaises(ValueError):
            self.v1 - self.v3

    def test_mul(self):
        self.assertEqual(self.v1 * 2, Vector(2, 4, 6))
        self.assertEqual(2 * self.v1, Vector(2, 4, 6))

    def test_truediv(self):
        self.assertEqual(self.v1 / 2, Vector(0.5, 1.0, 1.5))
        with self.assertRaises(ValueError):
            self.v1 / 0

    def test_dot(self):
        self.assertEqual(self.v1.dot(self.v2), 32)
        with self.assertRaises(ValueError):
            self.v1.dot(self.v3)

    def test_magnitude(self):
        self.assertAlmostEqual(self.v1.magnitude(), math.sqrt(14))

    def test_normalized(self):
        norm_v1 = self.v1.normalized()
        magnitude_norm_v1 = norm_v1.magnitude()
        self.assertAlmostEqual(magnitude_norm_v1, 1.0)
        with self.assertRaises(ValueError):
            self.zero_vector.normalized()

    def test_eq(self):
        self.assertTrue(self.v1 == Vector(1, 2, 3))
        self.assertFalse(self.v1 == self.v2)

    def test_len(self):
        self.assertEqual(len(self.v1), 3)
        self.assertEqual(len(self.v3), 2)

    def test_getitem(self):
        self.assertEqual(self.v1[0], 1)
        self.assertEqual(self.v1[1], 2)
        self.assertEqual(self.v1[2], 3)

    def test_setitem(self):
        v = Vector(1, 2, 3)
        v[0] = 4
        v[1] = 5
        v[2] = 6
        self.assertEqual(v, Vector(4, 5, 6))


if __name__ == '__main__':
    unittest.main()
