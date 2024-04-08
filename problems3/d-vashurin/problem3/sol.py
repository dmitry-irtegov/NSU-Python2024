import operator
from collections.abc import Iterable, Iterator
from functools import reduce
from typing import Generic, Protocol, Self, TypeVar, cast, overload


class Component(Protocol):
    def __add__(self, __value: Self) -> Self:
        ...

    def __sub__(self, __value: Self) -> Self:
        ...

    def __mul__(self, __value: Self) -> Self:
        ...

    def __str__(self) -> str:
        ...

    def __eq__(self, __value: object) -> bool:
        ...


C = TypeVar("C", bound=Component)


class Vector(Generic[C]):
    __slots__ = ("_components",)

    def __init__(self, components: Iterable[C]) -> None:
        self._components: tuple[C, ...] = tuple(components)

    @classmethod
    def from_literals(cls, *components: C) -> Self:
        return cls(components)

    def _check_equal_len(self, other):
        if len(self) != len(other):
            message = f"vectors have different length: {len(self) = } and {len(other) = }"
            raise ValueError(message)

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[C]:
        return iter(self._components)

    def __str__(self) -> str:
        return f"Vector({", ".join(map(str, self._components))})"

    @overload
    def __getitem__(self, __index: int) -> C: ...
    @overload
    def __getitem__(self, __index: slice) -> Self: ...
    def __getitem__(self, __index):
        if isinstance(__index, slice):
            return type(self)(self._components[__index])

        return self._components[__index]

    def __add__(self, __value: C | Self) -> Self:
        if isinstance(__value, Vector):
            self._check_equal_len(__value)
            return type(self)(a + b for a, b in zip(self, __value))

        component = cast(C, __value)
        return type(self)(a + component for a in self)

    def __sub__(self, __value: C | Self) -> Self:
        if isinstance(__value, Vector):
            self._check_equal_len(__value)
            return type(self)(a - b for a, b in zip(self, __value))

        component = cast(C, __value)
        return type(self)(a - component for a in self)

    @overload
    def __mul__(self, __value: C) -> Self: ...
    @overload
    def __mul__(self, __value: Self) -> C: ...
    def __mul__(self, __value):
        if isinstance(__value, Vector):
            self._check_equal_len(__value)
            return reduce(operator.add, (a * b for a, b in zip(self, __value)))

        component = cast(C, __value)
        return type(self)(a * component for a in self)

    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True

        if not isinstance(__value, Vector):
            return False

        return len(self) == len(__value) and all(a == b for a, b in zip(self, __value))
