import pytest

from sol import bound_seq


def test_floats():
    assert bound_seq([1.0, 2.4, 1.9, 5.6], 2.0, 3.0) == [2.0, 2.4, 2.0, 3.0]


def test_strs():
    assert bound_seq(["Orange", "Apple", "Ginger", "Tomato", "Lemon", "Pumpkin"], "Cucumber", "Potato")


def test_raises():
    with pytest.raises(ValueError):
        bound_seq([242, 29450], 100000, 104)
