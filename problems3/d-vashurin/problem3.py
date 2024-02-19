from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar, overload

N = TypeVar("N", int, float, int | float)


class Vector(Generic[N]):
    __slots__ = ("_components",)

    def __init__(self, components: Iterable[N]) -> None:
        self._components: tuple[N, ...] = tuple(components)

    @classmethod
    def from_literals(cls, *components: N) -> "Vector[N]":
        return cls(components)

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[N]:
        return iter(self._components)

    def __add__(self, __value: N | "Vector[N]") -> "Vector[N]":
        if isinstance(__value, Vector):
            assert len(self) == len(__value)
            return Vector(a + b for a, b in zip(self, __value))

        return Vector(a + __value for a in self)

    def __sub__(self, __value: N | "Vector[N]") -> "Vector[N]":
        if isinstance(__value, Vector):
            assert len(self) == len(__value)
            return Vector(a - b for a, b in zip(self, __value))

        return Vector(a - __value for a in self)

    @overload
    def __mul__(self, __value: N) -> "Vector[N]": ...
    @overload
    def __mul__(self, __value: "Vector[N]") -> N: ...
    def __mul__(self, __value):
        if isinstance(__value, Vector):
            assert len(self) == len(__value)
            return sum(a * b for a, b in zip(self, __value))

        return Vector(a * __value for a in self)

    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True

        if not isinstance(__value, Vector):
            return False

        assert len(self) == len(__value)
        return all(a == b for a, b in zip(self, __value))
