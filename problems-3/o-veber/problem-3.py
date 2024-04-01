from unittest import TestCase, main


class Vector:
    def __init__(self, *components):
        self._components = components
        self.len = len(components)

    def __add__(self, other):
        if isinstance(other, Vector):
            if other.len != self.len:
                raise ValueError("Vectors must be same length for \'add\' operation")
            return Vector(*(s + o for s, o in zip(self._components, other._components)))
        else:
            raise TypeError("Unsupported operation")

    def __sub__(self, other):
        if isinstance(other, Vector):
            if other.len != self.len:
                raise ValueError("Vectors must be same length for \'sub\' operation")
            return Vector(*(s - o for s, o in zip(self._components, other._components)))
        else:
            raise TypeError("Unsupported operation")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(s * o for s, o in zip(self._components, other._components))
        elif isinstance(other, (int, float, complex)):
            return Vector(*(s * other for s in self._components))
        else:
            raise TypeError("Unsupported operation")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._components == other._components
        return False

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        return self._components[index]

    def __str__(self):
        return f"Vector({', '.join(map(str, self._components))})"


class TestVector(TestCase):
    def test_adding(self):
        first = Vector(1, 2, 3)
        second = Vector(4, 5, 6)
        self.assertEqual(Vector(5, 7, 9), first + second)

    def test_adding_raises_type_error(self):
        first = Vector(1, 2, 3)
        second = 2
        self.assertRaises(TypeError, lambda: first + second)

    def test_adding_raises_value_error(self):
        first = Vector(1)
        second = Vector(1, 2)
        self.assertRaises(ValueError, lambda: first + second)

    def test_subtracting(self):
        first = Vector(1, 2, 3)
        second = Vector(4, 5, 6)
        self.assertEqual(Vector(3, 3, 3), second - first)

    def test_subtracting_raises_type_error(self):
        first = Vector(1, 2, 3)
        second = 2
        self.assertRaises(TypeError, lambda: first - second)

    def test_subtracting_raises_value_error(self):
        first = Vector(1)
        second = Vector(1, 2)
        self.assertRaises(ValueError, lambda: first - second)

    def test_scalar_mult(self):
        first = Vector(1, 2, 3)
        self.assertEqual(Vector(5, 10, 15), first * 5)

    def test_vector_mult(self):
        first = Vector(1, 2, 3)
        second = Vector(3, 3, 3)
        self.assertEqual(18, first * second)

    def test_mult_raises_exception(self):
        first = Vector(1, 2, 3)
        second = None
        self.assertRaises(TypeError, lambda: first * second)

    def test_len(self):
        first = Vector(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(7, first.len)

    def test_getitem(self):
        first = Vector(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(3, first[2])

    def test_equals(self):
        first = Vector(1, 2, 3)
        second = Vector(1, 2, 3)
        self.assertEqual(first, second)

    def test_not_equals(self):
        first = Vector(1, 2, 3)
        second = Vector(1, 2, 4)
        self.assertNotEqual(first, second)

    def test_not_equals_with_different_type(self):
        first = Vector(1, 2, 3)
        self.assertNotEqual(first, 2)

    def test_getitem_negative(self):
        first = Vector(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(3, first[-5])

    def test_getitem_raises_exception(self):
        first = Vector(1, 2, 3, 4, 5, 6, 7)
        self.assertRaises(IndexError, lambda: first[1000])

    def test_str(self):
        first = Vector(1, 2, 3)
        self.assertEqual('Vector(1, 2, 3)', first.__str__())


if __name__ == '__main__':
    main()
