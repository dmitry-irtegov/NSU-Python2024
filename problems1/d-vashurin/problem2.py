from collections.abc import MutableSequence
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from _typeshed import SupportsDunderGT, SupportsDunderLT

    Ordered = TypeVar("Ordered", SupportsDunderGT, SupportsDunderLT)


def bound_seq(
    seq: "MutableSequence[Ordered]",
    lower: "Ordered",
    upper: "Ordered",
) -> "MutableSequence[Ordered]":
    """Bound the provided mutable `seq` with the `lower` and `upper` bounds.

    >>> bound_seq([1.0, 2.4, 1.9, 5.6], 2.0, 3.0)
    [2.0, 2.4, 2.0, 3.0]
    >>> bound_seq(["Orange", "Apple", "Ginger", "Tomato", "Lemon", "Pumpkin"], "Cucumber", "Potato")
    ['Orange', 'Cucumber', 'Ginger', 'Potato', 'Lemon', 'Potato']
    >>> bound_seq([242, 29450], 100000, 104)
    Traceback (most recent call last):
        ...
    ValueError: lower = 100000 is greater than upper = 104

    All elements are changed in the following order:
    - if the element is lower than `lower`, it will be replaced with `lower`;
    - else if the element is greater than `upper`, it will be replaced with `upper`;
    - else the element remains in its place.

    Note:
        `lower` should be less or equal to `upper`.

    Raises:
        ValueError:
            If `lower` is greater than `upper`.
    """
    if lower > upper:
        message = f"{lower = } is greater than {upper = }"
        raise ValueError(message)

    for index, elem in enumerate(seq):
        if elem < lower:
            seq[index] = lower
        elif upper < elem:
            seq[index] = upper

    return seq
