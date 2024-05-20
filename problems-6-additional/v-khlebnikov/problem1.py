from functools import update_wrapper
from inspect import signature
import unittest


class Cache(object):
    def __init__(self, func):
        self.__func = func
        self.__cache = {}
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        arguments = signature(self.__func).bind(*args, **kwargs).arguments
        arguments.update(arguments.pop('kwargs', {}))
        arg_set = frozenset(arguments.items())
        if arg_set not in self.__cache:
            self.__cache[arg_set] = self.__func(*args, **kwargs)
        return self.__cache[arg_set]

    def get_cache(self):
        return self.__cache


class TestCacheDecorator(unittest.TestCase):
    def test_different_functions(self):
        @Cache
        def sum(a, b):
            return a + b
        
        @Cache
        def sub(a, b):
            return a - b
        
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sum(2, 3), 5)

        self.assertEqual(len(sum.get_cache()), 1)
        self.assertEqual(len(sub.get_cache()), 1)


    def test_different_order_kwargs(self):
        @Cache
        def some_count_func(x, y, z):
            return x * y - z
        
        self.assertEqual(some_count_func(2, 3, 4), 2)
        self.assertEqual(some_count_func(z=2, y=3, x=4), 10)
        self.assertEqual(some_count_func(x=2, y=3, z=4), 2)
        self.assertEqual(some_count_func(2, y=3, z=4), 2)
        self.assertEqual(some_count_func(2, 3, z=4), 2)
        self.assertEqual(some_count_func(x=2, y=3, z=4), some_count_func(2, 3, 4))

        self.assertEqual(len(some_count_func.get_cache()), 2)


    def test_similar_args(self):
        @Cache
        def sum(a, b):
            return a + b
        
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(1, b=2), 3)
        self.assertEqual(sum(a=1, b=2), 3)

        self.assertEqual(len(sum.get_cache()), 1)
        self.assertEqual(sum.get_cache(), {frozenset({("a", 1), ("b", 2)}): 3})


    def test_different_signatures(self):
        @Cache
        def strange_sum(a, b, *args, **kwargs):
            return a + b + sum(args) + sum(kwargs.values())
        
        self.assertEqual(strange_sum(1, 2), 3)
        self.assertEqual(strange_sum(1, 2), 3)
        self.assertEqual(strange_sum(1, c=1, b=2), 4)
        self.assertEqual(strange_sum(1, c=1, b=2), 4)
        self.assertEqual(strange_sum(1, 2, c=2, d=3), 8)
        self.assertEqual(strange_sum(1, 2, c=2, d=3), 8)
        self.assertEqual(strange_sum(1, 2, c=2, d=3, g=2, f=10), 20)
        self.assertEqual(strange_sum(1, 2, c=2, d=3, g=2, f=10), 20)
        
        self.assertEqual(len(strange_sum.get_cache()), 4)


if __name__ == "__main__":
    unittest.main()
