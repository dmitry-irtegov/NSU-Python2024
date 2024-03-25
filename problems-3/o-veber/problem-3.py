from unittest import TestCase, main


class Vector:
    def __init__(self, *components):
        self.components = components
        print(components)
        self.len = len(components)

    def __add__(self, other):
        if other.len != self.len:
            raise ValueError("Vectors must be same length for \'add\' operation")
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        if other.len != self.len:
            raise ValueError("Vectors must be same length for \'sub\' operation")
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Unsupported operation")

    def __eq__(self, other):
        return self.components == other.components

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if index > self.len:
            raise IndexError("Index must be less than vector size")
        return self.components[index]

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"


class TestVector(TestCase):
    def test_adding(self):
        first = Vector(1, 2, 3)
        second = Vector(4, 5, 6)
        self.assertEqual(Vector(5, 7, 9), first + second)

    def test_adding_raises_exception(self):
        first = Vector(1)
        second = Vector(1, 2)
        self.assertRaises(ValueError, lambda: first + second)

    def test_subtracting(self):
        first = Vector(1, 2, 3)
        second = Vector(4, 5, 6)
        self.assertEqual(Vector(3, 3, 3), second - first)

    def test_subtracting_raises_exception(self):
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
