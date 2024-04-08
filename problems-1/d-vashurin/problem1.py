from collections.abc import Iterable
from itertools import chain
from typing import Protocol, Self


class IntAddable(Protocol):
    def __add__(self, other: int | Self) -> int | Self:
        pass


def cumulative_sums(nums: Iterable[IntAddable]) -> list[IntAddable]:
    """Returns a some kind of cumulative sum of the ``nums``.

    >>> cumulative_sums((1, 2, 3))
    [0, 1, 3, 6]

    >>> cumulative_sums(range(10, 0, -2))
    [0, 10, 18, 24, 28, 30]

    >>> cumulative_sums([])
    [0]
    """

    current: IntAddable = 0
    return [current := n + current for n in chain([0], nums)]
