from typing import Sequence

from vector import Vector


def compare(a: Vector, b: Sequence[float]):
    assert len(a) == len(b)
    for act, exp in zip(a, b):
        assert act == exp


def compare_delta(a: Vector, b: Sequence[float], delta=0.000000001):
    assert len(a) == len(b)
    for act, exp in zip(a, b):
        assert -delta < act - exp < delta


class TestVector:
    def test_len_constructor(self):
        v = Vector(6)
        assert len(v) == 6
        for i in v:
            assert i == 0

    def test_value_constructor(self):
        v = Vector([1, 2, 3, 5])
        assert len(v) == 4
        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3
        assert v[3] == 5

    def test_setitem(self):
        arr = [1, 2, 3, 5]
        v = Vector(arr)
        compare(v, [1, 2, 3, 5])
        v[2] = 10
        compare(v, [1, 2, 10, 5])
        assert arr[2] == 3

    def test_clone(self):
        v = Vector([1, 2])
        clone = v.clone()
        assert len(clone) == 2
        v[1] = 9
        assert clone[1] == 2

    def test_iadd(self):
        v = Vector([10, 20, 30])
        v_save = v
        another = Vector([1, 2, 3])
        v += another
        compare(v, [11, 22, 33])
        compare(v_save, [11, 22, 33])
        compare(another, [1, 2, 3])

    def test_add(self):
        v = Vector([10, 20, 30])
        another = Vector([1, 2, 3])
        res = v + another
        compare(res, [11, 22, 33])
        compare(v, [10, 20, 30])
        compare(another, [1, 2, 3])

    def test_isub(self):
        v = Vector([10, 20, 30])
        v_save = v
        another = Vector([1, 2, 3])
        v -= another
        compare(v, [9, 18, 27])
        compare(v_save, [9, 18, 27])
        compare(another, [1, 2, 3])

    def test_sub(self):
        v = Vector([10, 20, 30])
        another = Vector([1, 2, 3])
        res = v - another
        compare(res, [9, 18, 27])
        compare(v, [10, 20, 30])
        compare(another, [1, 2, 3])

    def test_imul(self):
        v = Vector([10, 20, 30])
        v_save = v
        scalar = 5.01
        v *= scalar
        compare_delta(v, [50.1, 100.2, 150.3])
        compare_delta(v_save, [50.1, 100.2, 150.3])

    def test_mul(self):
        v = Vector([10, 20, 30])
        scalar = 1000
        res = v * scalar
        compare(res, [10000, 20000, 30000])
        compare(v, [10, 20, 30])

    def test_neg(self):
        v = Vector([10, 20, 30])
        res = -v
        compare(res, [-10, -20, -30])
        compare(v, [10, 20, 30])

    def test_eq(self):
        v = Vector([10, 20, 30])
        another = v.clone()
        assert v == another
        another[0], another[1] = another[1], another[0]
        assert v != another

    def test_dot(self):
        a = Vector([1, 4, 6])
        b = Vector([10, 11, 18])
        assert a.dot(b) == 162

    def test_abs(self):
        v = Vector([3, 12, 10, 6])
        assert abs(v) == 17
