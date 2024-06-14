import pytest

from sol import factorize


@pytest.mark.parametrize(
    ["number", "factors"],
    [
        (2, [(2, 1)]),
        (7, [(7, 1)]),
        (6, [(2, 1), (3, 1)]),
        (9, [(3, 2)]),
        (21, [(3, 1), (7, 1)]),
        (31, [(31, 1)]),
        (1_000_000_000_000_000_000_000, [(2, 21), (5, 21)]),
        (int(pow(2, 31) - 1), [(int(pow(2, 31)) - 1, 1)]),
    ]
)
def test_factoring(number: int, factors: list[tuple[int, int]]):
    assert factorize(number) == factors
