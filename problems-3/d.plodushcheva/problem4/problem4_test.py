import unittest
from problem4 import CartesianProductIterator


class TestCartesianProductIterator(unittest.TestCase):

    def test_get_current_element(self):
        x = [1, 2, 3]
        n = 2
        iterator = CartesianProductIterator(x, n)
        self.assertEqual(iterator.get_current_element(), (1, 1))

    def test_next_element(self):
        x = [1, 2, 3]
        n = 2
        iterator = CartesianProductIterator(x, n)

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (1, 2))

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (1, 3))

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (2, 1))

    def test_assert(self):
        x = [1, 2]
        n = 2
        iterator = CartesianProductIterator(x, n)
        iterator.next_element()
        iterator.next_element()
        iterator.next_element()

        with self.assertRaises(StopIteration):
            iterator.next_element()

    def test_cyclic_iterator(self):
        x = [1, 2]
        n = 2
        iterator = CartesianProductIterator(x, n, cyclic=True)

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (1, 2))

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (2, 1))

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (2, 2))

        iterator.next_element()
        self.assertEqual(iterator.get_current_element(), (1, 1))

    def test_stop_iteration_no_elements(self):
        x = []
        n = 2
        iterator = CartesianProductIterator(x, n)

        with self.assertRaises(StopIteration):
            iterator.next_element()


if __name__ == '__main__':
    unittest.main()
