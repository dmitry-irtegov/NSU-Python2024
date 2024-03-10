from unittest import TestCase, main


class Cachier(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args not in self.cache:
            self.cache[args] = self.func(*args, **kwargs)
        return self.cache[args]


class TestCachier(TestCase):
    def test_cache_function_value(self):
        cached = Cachier
        sum = cached(lambda x, y: x + y)
        self.assertEqual(sum.cache, {})
        self.assertEqual(3, sum(1, 2))
        self.assertEqual({(1, 2): 3}, sum.cache)
        self.assertEqual(3, sum(1, 2))
        self.assertEqual({(1, 2): 3}, sum.cache)

    def test_cache_function_many_values(self):
        cached = Cachier
        sum = cached(lambda x, y: x + y)
        self.assertEqual(sum.cache, {})
        self.assertEqual(3, sum(1, 2))
        self.assertEqual(5, sum(3, 2))
        self.assertEqual(2, sum(1, 1))
        self.assertEqual(sum.cache, {(1, 2): 3, (3, 2): 5, (1, 1): 2})


if __name__ == '__main__':
    main()
