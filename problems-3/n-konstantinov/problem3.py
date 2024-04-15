from unittest import TestCase
class Vector:
    def __init__(self, *data):
        self._data = data
        self.length = len(data)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for +")
        if self.length != other.length:
            raise ValueError("Vectors must have the same length for addition")
        return Vector(*(x + y for x, y in zip(self._data, other._data)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for -")
        if self.length != other.length:
            raise ValueError("Vectors must have the same length for subtraction")
        return Vector(*(x - y for x, y in zip(self._data, other._data)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.length != other.length:
                raise ValueError("Vectors must have the same length for dot product")
            return sum(x * y for x, y in zip(self._data, other._data))
        elif isinstance(other, (int, float, complex)):
            return Vector(*(x * other for x in self._data))
        else:
            raise TypeError("Unsupported operand type for *")

    def __eq__(self, other):
        return isinstance(other, Vector) and self._data == other._data

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        return f"Vector({', '.join(map(str, self._data))})"


class TestVector(TestCase):
    def test_init(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(v1, Vector(1, 2, 3))
        self.assertEqual(v1.length, 3)

        v2 = Vector()
        self.assertEqual(v2, Vector())
        self.assertEqual(v2.length, 0)

    def test_add(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v1 + v2
        self.assertEqual(v3, Vector(5, 7, 9))

        with self.assertRaises(TypeError):
            v1 + 123

        with self.assertRaises(ValueError):
            v1 + Vector(1, 2)

    def test_sub(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        v3 = v1 - v2
        self.assertEqual(v3, Vector(-3, -3, -3))

        with self.assertRaises(TypeError):
            v1 - 123

        with self.assertRaises(ValueError):
            v1 - Vector(1, 2)

    def test_mul(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        dot_product = v1 * v2
        self.assertEqual(dot_product, 32)

        v3 = v1 * 2
        self.assertEqual(v3, Vector(2, 4, 6))

        with self.assertRaises(ValueError):
            v1 * Vector(1, 2)

        with self.assertRaises(TypeError):
            v1 * "123"

    def test_eq(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(1, 2, 3)
        v3 = Vector(4, 5, 6)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == v3)
        self.assertFalse(v1 == 123)

    def test_len(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(len(v1), 3)

        v2 = Vector()
        self.assertEqual(len(v2), 0)

    def test_getitem(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(v1[0], 1)
        self.assertEqual(v1[1], 2)
        self.assertEqual(v1[2], 3)

        with self.assertRaises(IndexError):
            v1[3]

    def test_str(self):
        v1 = Vector(1, 2, 3)
        self.assertEqual(str(v1), "Vector(1, 2, 3)")

        v2 = Vector()
        self.assertEqual(str(v2), "Vector()")
