import pytest

from sol import collatz_conjecture


@pytest.mark.parametrize(
    "start, seq",
    [
        (17, [17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
        (6, [6, 3, 10, 5, 16, 8, 4, 2, 1]),
        (23, [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    ]
)
def test_collatz_conjecture(start: int, seq: list[int]) -> None:
    assert list(collatz_conjecture(start)) == seq


def test_invalid_values() -> None:
    with pytest.raises(ValueError):
        collatz_conjecture(0)

    with pytest.raises(ValueError):
        collatz_conjecture(-10)
