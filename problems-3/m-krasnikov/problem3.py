import unittest


class Vector:
    def __init__(self, *components):
        self._components = components

    def __add__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must have the same dimensions to perform addition.")
        return Vector(*(a + b for a, b in zip(self._components, other._components)))

    def __sub__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must have the same dimensions to perform subtraction.")
        return Vector(*(a - b for a, b in zip(self._components, other._components)))

    def __mul__(self, scalar):
        return Vector(*(scalar * x for x in self._components))

    def dot_product(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must have the same dimensions to compute dot product.")
        return sum(a * b for a, b in zip(self._components, other._components))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self._components == other._components

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]

    def __repr__(self):
        return f"Vector({self._components})"


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector1 = Vector(1, 2, 3)
        self.vector2 = Vector(4, 5, 6)
        self.vector3 = Vector(1, 2, 3)

    def test_addition(self):
        self.assertEqual(self.vector1 + self.vector2, Vector(5, 7, 9))

    def test_subtraction(self):
        self.assertEqual(self.vector2 - self.vector1, Vector(3, 3, 3))

    def test_scalar_multiplication(self):
        self.assertEqual(self.vector1 * 2, Vector(2, 4, 6))

    def test_dot_product(self):
        self.assertEqual(self.vector1.dot_product(self.vector2), 32)

    def test_equality(self):
        self.assertEqual(self.vector1, self.vector3)
        self.assertNotEqual(self.vector1, self.vector2)

    def test_length(self):
        self.assertEqual(len(self.vector1), 3)

    def test_indexing(self):
        self.assertEqual(self.vector1[0], 1)
        self.assertEqual(self.vector1[1], 2)
        self.assertEqual(self.vector1[2], 3)


if __name__ == "__main__":
    unittest.main()
