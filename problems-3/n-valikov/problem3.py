import unittest
from numbers import Number
from itertools import starmap
from typing import Tuple


class Vector:
    _content: Tuple
    _iter_counter: int

    def __init__(self, content: Tuple):
        if not isinstance(content, tuple) or not all(map(lambda value: isinstance(value, Number), content)):
            raise TypeError("content must be a list of values that inherit from Number")

        self._content = content
        self._iter_counter = 0

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError('other must be of type Vector')
        if len(self) != len(other):
            raise ValueError('Vectors dimensions must be equal')

        return Vector((*[first + second for first, second in zip(self._content, other._content)],))

    def __sub__(self, other) -> 'Vector':
        return self + (-other)

    def __neg__(self) -> 'Vector':
        # UncheckedWarning
        return Vector(tuple(-value for value in self._content))

    def __mul__(self, constant: int) -> 'Vector':
        new_vector_content = list(self._content)
        for index in range(len(self)):
            new_vector_content[index] *= constant

        return Vector((*new_vector_content,))

    def __next__(self):
        length = len(self)
        index = 0
        while index < length:
            yield self[index]
            index += 1

    def __getitem__(self, item: int) -> Number:
        if not isinstance(item, int):
            raise TypeError('item must be an integer')

        return self._content[item]

    def __len__(self):
        return len(self._content)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            return False

        return all(starmap(lambda x_1, x_2: x_1 == x_2, zip(self._content, other._content)))

    def __str__(self):
        return (f"Number of dimensions: {len(self._content)}\n"
                f"{'\n'.join(map(lambda value: str(value), self._content))}\n")

    def scalar_product(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError('other must be of type Vector')
        if len(self) != len(other):
            raise ValueError('Vectors dimensions must be equal')

        new_vector_content = list(self._content)

        for index, value in enumerate(other._content):
            new_vector_content[index] *= value

        return Vector(tuple(new_vector_content))


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector_1 = Vector((1, 2, 3))
        self.vector_2 = Vector((3, 4, 5, 6, 7))
        self.vector_4 = Vector((7, 6, 5))

    def test_constructor(self):
        self.assertEqual(self.vector_1._content[0], 1)
        self.assertEqual(self.vector_1._content[1], 2)
        self.assertEqual(self.vector_1._content[2], 3)

        with self.assertRaises(TypeError):
            Vector((1, "stre"))
        with self.assertRaises(TypeError):
            Vector([1, 2, 3])

    def test_add(self):
        self.assertEqual(self.vector_1 + self.vector_4, Vector((8, 8, 8)))

        with self.assertRaises(TypeError):
            self.vector_1 + 4

        with self.assertRaises(ValueError):
            self.vector_1 + self.vector_2

    def test_sub(self):
        self.assertEqual(self.vector_1 - self.vector_4, -self.vector_4 + self.vector_1)

    def test_neg(self):
        tmp_vec = -self.vector_1

        self.assertEqual(tmp_vec[0], -self.vector_1._content[0])
        self.assertEqual(tmp_vec[1], -self.vector_1._content[1])
        self.assertEqual(tmp_vec[2], -self.vector_1._content[2])

    def test_mul(self):
        tmp_vec = self.vector_1 * 4

        self.assertEqual(tmp_vec[0], 4)
        self.assertEqual(tmp_vec[1], 8)
        self.assertEqual(tmp_vec[2], 12)

    def test_get(self):
        self.assertEqual(self.vector_1[0], self.vector_1._content[0])
        self.assertEqual(self.vector_1[1], self.vector_1._content[1])
        self.assertEqual(self.vector_1[2], self.vector_1._content[2])

        with self.assertRaises(TypeError):
            self.vector_1["hehe"]

    def test_len(self):
        self.assertEqual(len(self.vector_1), len(self.vector_1._content))

    def test_eq(self):
        self.assertTrue(self.vector_1 == Vector((1, 2, 3)))
        self.assertFalse(self.vector_1 == self.vector_2)

        with self.assertRaises(TypeError):
            self.vector_1 == "lolchik"

    def test_scalar_product(self):
        self.assertEqual(self.vector_1.scalar_product(self.vector_4), Vector((7, 12, 15)))

        with self.assertRaises(TypeError):
            self.vector_1.scalar_product("diablo")
        with self.assertRaises(ValueError):
            self.vector_1.scalar_product(self.vector_2)


if __name__ == '__main__':
    unittest.main()
