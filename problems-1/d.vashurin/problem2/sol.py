from collections.abc import MutableSequence
from typing import Protocol, TypeVar

T_contra = TypeVar("T_contra", contravariant=True)


class SupportsDunderLT(Protocol[T_contra]):
    def __lt__(self, other: T_contra, /) -> bool:
        ...

class SupportsDunderGT(Protocol[T_contra]):
    def __gt__(self, other: T_contra, /) -> bool:
        ...


Ordered = TypeVar("Ordered", SupportsDunderGT, SupportsDunderLT)


def bound_seq(
    seq: MutableSequence[Ordered],
    lower: Ordered,
    upper: Ordered,
) -> MutableSequence[Ordered]:
    """Bound the provided mutable `seq` with the `lower` and `upper` bounds.

    All elements are changed in the following order:
    - if the element is lower than `lower`, it will be replaced with `lower`;
    - else if the element is greater than `upper`, it will be replaced with `upper`;
    - else the element remains in its place.

    Note:
        `lower` should be less or equal to `upper`.
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
