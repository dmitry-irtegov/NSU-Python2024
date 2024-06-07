import math
from abc import abstractmethod
from typing import overload, Sequence, Self, SupportsFloat, Iterable


class Vector(Sequence):
    _value: list[float]

    @overload
    def __init__(self, size: int):
        ...

    @overload
    def __init__(self, value: Sequence[SupportsFloat]):
        ...

    def __init__(self, x):
        if isinstance(x, int):
            self._value = [0] * x
        elif isinstance(x, Sequence):
            self._value = [float(i) for i in x]
        else:
            raise TypeError(f'constructor argument must be an integer or a sequence, not \'{type(x)}\'')

    @overload
    @abstractmethod
    def __getitem__(self, index: int) -> float:
        ...

    @overload
    @abstractmethod
    def __getitem__(self, index: slice) -> Sequence[float]:
        ...

    def __getitem__(self, index):
        return self._value[index]

    @overload
    @abstractmethod
    def __setitem__(self, index: int, value: float) -> None:
        ...

    @overload
    @abstractmethod
    def __setitem__(self, index: slice, value: Iterable[float]) -> None:
        ...

    def __setitem__(self, index, value):
        self._value[index] = value

    def __len__(self) -> int:
        return len(self._value)

    def clone(self) -> Self:
        return Vector(self._value)

    def __repr__(self) -> str:
        return f'Vector({repr(self._value)})'

    def __str__(self) -> str:
        return f'Vector[{', '.join(map(str, self._value))}]'

    def __iadd__(self, other: Self) -> Self:
        for i in range(len(self._value)):
            self._value[i] += other._value[i]
        return self

    def __add__(self, other: Self) -> Self:
        ret = self.clone()
        ret += other
        return ret

    def __isub__(self, other: Self) -> Self:
        for i in range(len(self._value)):
            self._value[i] -= other._value[i]
        return self

    def __sub__(self, other: Self) -> Self:
        ret = self.clone()
        ret -= other
        return ret

    def __imul__(self, scalar: SupportsFloat) -> Self:
        scalar = float(scalar)
        for i in range(len(self._value)):
            self._value[i] *= scalar
        return self

    def __mul__(self, scalar: SupportsFloat) -> Self:
        ret = self.clone()
        ret *= scalar
        return ret

    def __neg__(self) -> Self:
        return self * -1

    def __eq__(self, other: Self) -> bool:
        for i in zip(self._value, other._value):
            if i[0] != i[1]:
                return False
        return True

    def dot(self, other: Self) -> float:
        return sum(map(lambda t: t[0] * t[1], zip(self._value, other._value)))

    def __abs__(self) -> float:
        return math.sqrt(self.dot(self))
