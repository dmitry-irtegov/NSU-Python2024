import math


class Vector:

    def __init__(self, args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
        self.size = len(args)

    def add(self, other):
        for i in range(self.size):
            self.values[i] += other.get(i)

    def sub(self, other):
        for i in range(self.size):
            self.values[i] -= other.get(i)

    def scalar_mul(self, scalar):
        for i in range(self.size):
            self.values[i] *= scalar

    def mult(self, other):
        for i in range(self.size):
            self.values[i] *= other.get(i)

    def dot(self, other):
        dot_product = 0
        for i in range(self.size):
            dot_product += self.values[i] * other.get(i)
        return dot_product

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
