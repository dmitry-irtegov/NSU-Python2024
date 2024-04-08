import pytest

from sol import Vector


@pytest.fixture
def a() -> range:
    return range(0, 10, 1)


@pytest.fixture
def b() -> range:
    return range(0, 20, 2)


def test_addition(a: range, b: range) -> None:
    assert (Vector(a) + Vector(b))._components == Vector((a + b for a, b in zip(a, b)))._components


def test_subtraction(a: range, b: range) -> None:
    assert (Vector(a) - Vector(b))._components == Vector((a - b for a, b in zip(a, b)))._components


def test_scalar_multiplication(a: range, b: range) -> None:
    assert Vector(a) * Vector(b) == sum(a * b for a, b in zip(a, b))


def test_dot_multiplication(a: range, b: range) -> None:
    assert (Vector(components=a) * 2)._components == Vector(b)._components


def test_equality(a: range, b: range) -> None:
    assert Vector(a) + Vector(a) == Vector(b)


def test_string_representation(a: range) -> None:
    assert str(Vector(a)) == "Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)"


def test_indexing(a: range) -> None:
    assert Vector(a)[0] == 0
    assert Vector(a)[::-1] == Vector(a[::-1])
