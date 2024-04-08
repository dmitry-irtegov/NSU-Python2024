import math


class Vector:

    def __init__(self, *values):
        self._values = values
        self._size = len(values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both objects must be of one type")
        if len(self._values) != len(other._values):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(x + y for x, y in zip(self._values, other._values)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both objects must be of one type")
        if len(self._values) != len(other._values):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(x - y for x, y in zip(self._values, other._values)))

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float, complex)):
            return Vector(*(x * scalar for x in self._values))
        else:
            raise TypeError("Inappropriate operand type. Must be: int, float or complex")

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both objects must be of one type")
        if len(self._values) != len(other._values):
            raise ValueError("Vectors must have the same dimensions")
        return sum(x * y for x, y in zip(self._values, other._values))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._values == other._values
        return False

    def length(self):
        return math.sqrt(self.dot(self))

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        return self._values[item]

    def __str__(self):
        return "[" + ", ".join(map(str, self._values)) + "]"
