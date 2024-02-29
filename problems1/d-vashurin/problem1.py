from collections.abc import Iterable
from itertools import chain
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeVar

    from _typeshed import SupportsAdd

    A = TypeVar("A", bound=SupportsAdd)


def cumulative_sums(nums: "Iterable[A]") -> "list[A]":
    """Returns the cumulative sum of the `nums` iterable.

    >>> cumulative_sums((1, 2, 3))
    [1, 3, 6]

    >>> cumulative_sums(range(10, 0, -2))
    [10, 18, 24, 28, 30]

    >>> cumulative_sums([])
    []

    >>> cumulative_sums(["Hello", ", ", "World", "!"])
    ['Hello', 'Hello, ', 'Hello, World', 'Hello, World!']
    """

    iterator = iter(nums)

    try:
        current = next(iterator)
    except StopIteration:
        return []
    else:
        return list(chain([current], ((current := current + a) for a in iterator)))
