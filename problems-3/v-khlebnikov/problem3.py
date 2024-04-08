import unittest


class Vector:
    def __init__(self, *values):
        self._values = values
        self._length = len(values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both objects must be of one type")
        if self._length != other._length:
            raise ValueError("Both vectors must have the same dimensions")
        return Vector(*(x + y for x, y in zip(self._values, other._values)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both operands must be of one type")
        if self._length != other._length:
            raise ValueError("Both vectors must have the same dimensions")
        return Vector(*(x - y for x, y in zip(self._values, other._values)))

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector(*(other * x for x in self._values))
        elif isinstance(other, Vector):
            if self._length != other._length:
                raise ValueError("Both vectors must have the same dimensions")
            return Vector(*(x * y for x, y in zip(self._values, other._values)))
        else:
            raise TypeError("Inappropriate operand type")

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self._values == other._values

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        return self._values[item]

    def __str__(self):
        return "Vector{" + ", ".join(map(str, self._values)) + "}"


class TestVector(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Vector(5, 6, 7), Vector(1, 4, 3) + Vector(4, 2, 4))

    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2, 3) + 3

    def test_add_value_error(self):
        with self.assertRaises(ValueError):
            Vector(1, 2, 3) + Vector(1, 2)

    def test_sub(self):
        self.assertEqual(Vector(1, 4, 3), Vector(5, 6, 7) - Vector(4, 2, 4))

    def test_sub_type_error(self):
        with self.assertRaises(TypeError):
            Vector(1, 2, 3) - 3

    def test_sub_value_error(self):
        with self.assertRaises(ValueError):
            Vector(1, 2, 3) - Vector(1, 2)

    def test_mul_const_int(self):
        self.assertEqual(Vector(2, 4, 6), Vector(1, 2, 3) * 2)

    def test_mul_const_float(self):
        self.assertEqual(Vector(2.5, 5, 7.5), Vector(1, 2, 3) * 2.5)

    def test_mul_const_complex(self):
        self.assertEqual(Vector(2 + 3j, 4 + 6j, 6 + 9j), Vector(1, 2, 3) * (2 + 3j))

    def test_mul_scalar(self):
        self.assertEqual(Vector(43, 46, 30), Vector(43, 23, 10) * Vector(1, 2, 3))

    def test_mul_type_error(self):
        with self.assertRaises(TypeError):
            Vector(3) * "string"

    def test_mul_value_error(self):
        with self.assertRaises(ValueError):
            Vector(1, 2, 3) * Vector(1, 2)

    def test_eq(self):
        self.assertTrue(Vector(4, 3) == Vector(4, 3))

    def test_eq_with_another_type(self):
        self.assertTrue(Vector(4, 3) != 43)

    def test_not_eq(self):
        self.assertTrue(Vector(4, 3) != Vector(3, 4))

    def test_len(self):
        self.assertEqual(3, len(Vector(1, 2, 3)))

    def test_getitem(self):
        self.assertEqual(2, Vector(1, 2, 3)[1])

    def test_getitem_index_error(self):
        with self.assertRaises(IndexError):
            Vector()[0]

    def test_str(self):
        self.assertEqual("Vector{1, 2, 3}", str(Vector(1, 2, 3)))
