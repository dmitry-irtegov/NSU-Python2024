import pytest

from sol import primes


@pytest.mark.parametrize(
    "bound, expected",
    [
        (2, [2]),
        (10, [2, 3, 5, 7]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    ],
)
def test_primes(bound: int, expected: list[int]) -> None:
    assert primes(bound) == expected
