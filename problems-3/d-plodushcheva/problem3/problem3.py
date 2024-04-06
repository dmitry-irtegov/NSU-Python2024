import math


class Vector:

    def __init__(self, *values):
        self.values = values
        self.size = len(values)

    def __add__(self, other):
        new_values = [x + y for x, y in zip(self.values, other.values)]
        return Vector(*new_values)

    def __sub__(self, other):
        new_values = [x - y for x, y in zip(self.values, other.values)]
        return Vector(*new_values)

    def __mul__(self, scalar):
        new_values = [x * scalar for x in self.values]
        return Vector(*new_values)

    def dot(self, other):
        return sum(x * y for x, y in zip(self.values, other.values))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.values == other.values
        return False

    def length(self):
        return math.sqrt(self.dot(self))

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        return self.values[item]

    def __str__(self):
        return "[" + ", ".join(map(str, self.values)) + "]"
