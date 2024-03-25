from typing import Self
import unittest

class CartesianProductElement():
    _set: tuple
    _n: int
    _current_item_id: int
    _next_item_id: int
    _state: tuple

    def __init__(self, init_set: tuple, n: int, start_subset: tuple = (None,)) -> None:
        self._set = init_set
        self._n = n
        self._current_item_id = 0
        self._next_item_id = 1
        self._first = self._set[0]
        self._last = self._set[-1]
        if start_subset != (None,):
            self._state = start_subset
        else:
            self._state = tuple([self._first] * n)

    def next_subset(self) -> Self:
        next_state = list(self._state)
        next_item = self._set[self._next_item_id]
        next_state[self._current_item_id] = next_item
        next_state = tuple(next_state)

        if self._next_item_id == self._n - 1:
            self.
        try:
            # search from the end
            ni, cur_elem = next((self._n - i - 1, elem) for i, elem in enumerate(self._state[::-1]) if elem != self._last)
        except StopIteration:   # this was the last element in the product
            return CartesianProductElement(self._set, self._n)
        
        next_elem = self._next_elem(cur_elem)
        new_state = tuple([elem if i < ni else next_elem if i == ni else self._first for i, elem in enumerate(self._state)])

        return CartesianProductElement(self._set, self._n, new_state)
    
    def get_state(self) -> tuple:
        return self._state

    def __str__(self):
        return self._state.__str__()


class TestCartesianProduct(unittest.TestCase):
    def test_example(self):
        cp = CartesianProductElement((1, "a"), 2)
        test_cps = (cp.get_state(), ) 
        for _ in range(3):
            cp = cp.next_subset()
            test_cps += (cp.get_state(), )

        self.assertEqual(test_cps, ((1,1),(1,"a"),("a",1),("a","a")))

        test_cps += (cp.next_subset().get_state(), )
        self.assertEqual(test_cps, ((1,1),(1,"a"),("a",1),("a","a"),(1,1)))

    def test_single(self):
        cp = CartesianProductElement((0, ), 5)
        test_cps = (cp.get_state(), )
        test_cps += (cp.next_subset().get_state(), )
        self.assertEqual(test_cps, ((0,0,0,0,0),(0,0,0,0,0)))

    def test_4bit_nums(self):
        cp = CartesianProductElement((0,1), 4)
        test_cps = (cp.get_state(), )
        for _ in range(16):
            cp = cp.next_subset()
            test_cps += (cp.get_state(), )
            
        self.assertEqual(test_cps, (
            (0, 0, 0, 0),
            (0, 0, 0, 1),
            (0, 0, 1, 0),
            (0, 0, 1, 1),
            (0, 1, 0, 0),
            (0, 1, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 1, 1),
            (1, 0, 0, 0),
            (1, 0, 0, 1),
            (1, 0, 1, 0),
            (1, 0, 1, 1),
            (1, 1, 0, 0),
            (1, 1, 0, 1),
            (1, 1, 1, 0),
            (1, 1, 1, 1),
            (0, 0, 0, 0)))

if __name__ == "__main__":
    unittest.main()