from unittest import TestCase, main
from inspect import signature


class Cachier(object):
    def __init__(self, func):
        self._func = func
        self._cache = {}

    def get_cache(self):
        return self._cache

    def __call__(self, *args, **kwargs):
        cached_args = tuple()
        arg_names = signature(self._func).parameters
        for named_positional_arg in list(zip(arg_names, args)):
            cached_args += named_positional_arg
        for item in sorted(kwargs.items(), key=lambda x: x[0]):
            cached_args += item
        if cached_args not in self._cache:
            self._cache[cached_args] = self._func(*args, **kwargs)
        return self._cache[cached_args]


def my_sum(first, second):
    return first + second


@Cachier
def my_decorated_cached_sum(first, second):
    return first + second


class TestCachier(TestCase):

    def test_mixed_decorated_cache(self):
        self.assertEqual(3, my_decorated_cached_sum(1, 2))
        self.assertEqual(3, my_decorated_cached_sum(1, second=2))
        self.assertEqual(3, my_decorated_cached_sum(first=1, second=2))
        self.assertEqual({('first', 1, 'second', 2): 3}, my_decorated_cached_sum.get_cache())

    def test_mixed_cache(self):
        cached = Cachier
        cached_sum = cached(my_sum)
        self.assertEqual(3, cached_sum(1, 2))
        self.assertEqual(3, cached_sum(1, second=2))
        self.assertEqual(3, cached_sum(first=1, second=2))
        self.assertEqual({('first', 1, 'second', 2): 3}, cached_sum.get_cache())

    def test_cache_function_value(self):
        cached = Cachier
        cached_sum = cached(my_sum)
        self.assertEqual(cached_sum.get_cache(), {})

        self.assertEqual(3, cached_sum(1, 2))
        self.assertEqual({('first', 1, 'second', 2): 3}, cached_sum.get_cache())

        self.assertEqual(3, cached_sum(1, 2))
        self.assertEqual({('first', 1, 'second', 2): 3}, cached_sum.get_cache())

    def test_cache_function_many_values(self):
        cached = Cachier
        cached_sum = cached(my_sum)
        self.assertEqual(cached_sum.get_cache(), {})

        self.assertEqual(3, cached_sum(1, 2))
        self.assertEqual(3, cached_sum(1, 2))

        self.assertEqual(5, cached_sum(3, 2))
        self.assertEqual(5, cached_sum(3, 2))

        self.assertEqual(2, cached_sum(1, 1))
        self.assertEqual(2, cached_sum(1, 1))

        self.assertEqual(
            cached_sum.get_cache(),
            {('first', 1, 'second', 1): 2, ('first', 1, 'second', 2): 3, ('first', 3, 'second', 2): 5}
        )

    def test_cache_with_positional_arguments(self):
        cached = Cachier
        cached_sum = cached(my_sum)
        self.assertEqual(cached_sum.get_cache(), {})
        self.assertEqual(3, cached_sum(first=1, second=2))
        self.assertEqual(3, cached_sum(first=1, second=2))

        self.assertEqual(5, cached_sum(first=3, second=2))
        self.assertEqual(5, cached_sum(first=3, second=2))

        self.assertEqual(2, cached_sum(first=1, second=1))
        self.assertEqual(2, cached_sum(first=1, second=1))

        self.assertEqual(
            cached_sum.get_cache(),
            {('first', 1, 'second', 1): 2, ('first', 1, 'second', 2): 3, ('first', 3, 'second', 2): 5}
        )


if __name__ == '__main__':
    main()
