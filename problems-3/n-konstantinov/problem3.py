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
