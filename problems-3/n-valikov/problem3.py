from numbers import Number
from itertools import starmap
from typing import List, Tuple


class Vector(Number):
    content: Tuple[Number]
    iter_counter: int

    def __init__(self, content: Tuple[Number]):
        if not isinstance(content, Tuple) or not all(map(lambda value: isinstance(value, Number), content)):
            raise TypeError("content must be a list of values that inherit from Number")

        self.content = content
        self.iter_counter = 0

    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError('other must be of type Vector')
        if len(self) != len(other):
            raise ValueError('Vectors dimensions must be equal')

        new_vector_content: List[Number] = list(self.content)
        for index, value in enumerate(other):
            new_vector_content[index] += value

        return Vector((*new_vector_content,))

    def __sub__(self, other) -> 'Vector':
        return -self + other

    def __neg__(self) -> 'Vector':
        # UncheckedWarning
        return Vector(tuple(-value for value in self.content))

    def __mul__(self, constant: int) -> 'Vector':
        new_vector_content = list(self.content)
        for index in range(len(self)):
            new_vector_content[index] *= constant

        return Vector((*new_vector_content,))

    def __iter__(self):
        return self

    def __next__(self) -> Number:
        if self.iter_counter >= len(self.content):
            self.iter_counter = 0
            raise StopIteration
        else:
            self.iter_counter += 1
            return self.content[self.iter_counter - 1]

    def __getitem__(self, item: int) -> Number:
        if not isinstance(item, int):
            raise TypeError('item must be an integer')
        if item < 0 or item > len(self.content):
            raise ValueError('item must be between 0 and vector length')

        return self.content[item]

    def __len__(self):
        return len(self.content)

    def __eq__(self, other: 'Vector') -> bool:
        if not isinstance(other, Vector):
            raise TypeError('other must be of type Vector')

        if len(self) != len(other):
            return False

        return all(starmap(lambda x_1, x_2: x_1 == x_2, zip(self, other)))

    def __str__(self):
        return (f"Number of dimensions: {len(self.content)}\n"
                f"{'\n'.join(map(lambda value: str(value), self.content))}\n")

    def scalar_product(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError('other must be of type Vector')
        if len(self) != len(other):
            raise ValueError('Vectors dimensions must be equal')

        new_vector_content = list(self.content)

        for index, value in enumerate(other):
            new_vector_content[index] *= value

        return Vector(tuple(new_vector_content))


if __name__ == '__main__':
    v_1 = Vector((1, 2, 3, 4))
    v_2 = Vector((4, 3, 2, 1))

    print(v_1)
    print(v_2)

    print(v_1 + v_2)
    print(v_1 - v_2)
    print(v_1 * 5)
    print(v_1.scalar_product(v_2))

    print(v_1[3])
    print()
    
    print(v_1 == v_2)
