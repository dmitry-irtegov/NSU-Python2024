import math


class Vector:

    def __init__(self, args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
        self.size = len(args)

    def __add__(self, other):
        return [x + y for x, y in zip(self.values, other.values)]

    def __sub__(self, other):
        return [x - y for x, y in zip(self.values, other.values)]

    def __mul__(self, scalar):
        return [x * scalar for x in self.values]

    def mult(self, other):
        self.values = [x * y for x, y in zip(self.values, other.values)]

    def dot(self, other):
        return sum(x * y for x, y in zip(self.values, other.values))

    def compare(self, other):
        return self.values == other.values

    def length(self):
        s = 0
        for v in self.values:
            s += v ** 2
        return math.sqrt(s)

    def get(self, i):
        return self.values[i]

    def __str__(self):
        return "[" + ", ".join(map(str, self.values)) + "]"
