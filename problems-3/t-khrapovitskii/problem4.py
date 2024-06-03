from collections.abc import Sequence
from typing import overload, Any


class Cartesian(Sequence):
    def __init__(self, x: Sequence, n: int):
        if len(x) < 1:
            raise ValueError("Set of possible elements should be not empty")
        if n < 1:
            raise ValueError("Number of elements should be greater than zero")
        self._x = tuple(x)
        self._n = n
        self._state: list = [self._x[-1]] * n
        self._generator = self._next_state()
        self.next_state()

    def _next_state(self, cur_index=0):
        if cur_index != self._n - 1:
            for i in self._x:
                self._state[cur_index] = i
                yield from self._next_state(cur_index + 1)
            self._state[cur_index] = self._x[0]
        else:
            for i in self._x:
                self._state[cur_index] = i
                yield

    def next_state(self):
        try:
            next(self._generator)
            return
        except StopIteration:
            self._generator = self._next_state()
            self.next_state()
            return

    @overload
    def __getitem__(self, index: int) -> Any:
        return self._state[index]

    @overload
    def __getitem__(self, index: slice) -> Sequence[Any]:
        return self._state[index]

    def __getitem__(self, index):
        return self._state[index]

    def __len__(self):
        return self._n


class TestCartesian:
    def test_init(self):
        numbers = [1, 2, 3]
        cartesian = Cartesian(numbers, 3)
        for i in cartesian:
            assert i == 1

    def test_next_one(self):
        numbers = [1, 2, 3]
        cartesian = Cartesian(numbers, 1)
        assert cartesian[0] == 1
        cartesian.next_state()
        assert cartesian[0] == 2
        cartesian.next_state()
        assert cartesian[0] == 3
        cartesian.next_state()
        assert cartesian[0] == 1

    def test_next_two(self):
        numbers = [1, 2]
        cartesian = Cartesian(numbers, 3)
        for i in zip(cartesian, [1, 1]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 2]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [2, 1]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [2, 2]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 1]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 2]):
            assert i[0] == i[1]

    def test_next_three_start(self):
        numbers = [1, 2, 3]
        cartesian = Cartesian(numbers, 3)
        for i in zip(cartesian, [1, 1, 1]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 1, 2]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 1, 3]):
            assert i[0] == i[1]
        cartesian.next_state()
        for i in zip(cartesian, [1, 2, 1]):
            assert i[0] == i[1]

    def test_tree_full(self):
        numbers = [0, 1, 2]
        cartesian = Cartesian(numbers, 3)
        codes = set(range(3 ** 3))
        for i in range(3 ** 3):
            code = cartesian[0] * 9 + cartesian[1] * 3 + cartesian[2]
            codes.remove(code)
            cartesian.next_state()
        assert len(codes) == 0
        assert tuple(cartesian) == (0, 0, 0)
        cartesian.next_state()
        assert tuple(cartesian) == (0, 0, 1)
