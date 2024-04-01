import unittest

class n_ary_digit():
    _n: int
    _val: int

    def __init__(self, n: int):
        self._n = n
        self._val = 0

    def value(self) -> int:
        return self._val

    def inc(self) -> bool:
        if self._val == self._n - 1:
            self._val = 0
            return True
        self._val += 1
        return False

def increment_n_ary_list(num: list[n_ary_digit]) -> list[n_ary_digit]:
    for digit in num:
       overflown = digit.inc()
       if not overflown:
           return num
       
    return num

class CartesianProductElement():
    _set: tuple
    _n: int
    _ids: list[n_ary_digit]
    _current_item_id: int
    _next_item_id: int

    def __init__(self, init_set: tuple, n: int):
        self._set = init_set
        self._n = n
        self._first = self._set[0]
        self._last = self._set[-1]
        self._current_item_id = 0
        self._next_item_id = 1

        self._ids = [n_ary_digit(len(self._set)) for _ in range(n)]

    def next_subset(self):
        # state is m-ary number of length N - to get next elem we just increment it
        next_ids = increment_n_ary_list(self._ids)

        next_subset = CartesianProductElement(self._set, self._n)
        next_subset._ids = next_ids
        return next_subset
    
    def get_state(self) -> tuple:
        return tuple([self._set[i.value()] for i in self._ids])

    def __str__(self):
        return self.get_state().__str__()


class TestCartesianProduct(unittest.TestCase):
    def test_example(self):
        cp = CartesianProductElement((1, "a"), 2)
        test_cps = (cp.get_state(), ) 
        for _ in range(3):
            cp = cp.next_subset()
            test_cps += (cp.get_state(), )

        self.assertCountEqual(test_cps, ((1,1),(1,"a"),("a",1),("a","a")))

        test_cps += (cp.next_subset().get_state(), )
        self.assertCountEqual(test_cps, ((1,1),(1,"a"),("a",1),("a","a"),(1,1)))

    def test_single(self):
        cp = CartesianProductElement((0, ), 5)
        test_cps = (cp.get_state(), )
        test_cps += (cp.next_subset().get_state(), )
        self.assertCountEqual(test_cps, ((0,0,0,0,0),(0,0,0,0,0)))

    def test_4bit_nums(self):
        cp = CartesianProductElement((0,1), 4)
        test_cps = (cp.get_state(), )
        for _ in range(16):
            cp = cp.next_subset()
            test_cps += (cp.get_state(), )
            
        self.assertCountEqual(test_cps, (
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
