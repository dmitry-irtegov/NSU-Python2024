import unittest

def cached(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args[0]}")
            return cache[args]
        print(f"Calculating result for {args[0]}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cached
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


class TestCachedDecorator(unittest.TestCase):
    def test_cached_decorator(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(30), 832040)


if __name__ == '__main__':
    unittest.main()
