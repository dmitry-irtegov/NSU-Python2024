import unittest
import sys
import inspect
import time
from time import sleep
from functools import wraps


def cached(func):
    cache = {}

    @wraps(func)
    def decorated(*args, **kwargs):
        key = (
            args,
            tuple(sorted(kwargs.items()))
        )
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return decorated


class CachedTest(unittest.TestCase):
    def test_cached_same_results(self):
        payload_function = lambda x: x + 1

        @cached
        def some_function(x):
            return x + 1

        for arg in range(100):
            self.assertEqual(
                payload_function(arg),
                some_function(arg)
            )

    def test_different_args(self):
        @cached
        def some_function(*args, **kwargs):
            return ' '.join(map(str, args)) + ';' + ' '.join(map(str, kwargs.items()))

        expectedAnswer = "1 2 3;('one', 'two') ('three', 'four')"

        self.assertEqual(
            expectedAnswer,
            some_function('1', '2', '3', one='two', three='four')
        )

        self.assertEqual(
            expectedAnswer,
            some_function('1', '2', '3', three='four', one='two')
        )


def run_benchmark():
    print("Running demo benchmark")

    @cached
    def dummy_long_computation(x):
        print("Sleeping")
        sleep(5)
        return x

    print("Running the following function twice with the same arg: ")
    print(inspect.getsource(dummy_long_computation))

    print("Computing result for x=1 for the first time:")
    print(dummy_long_computation(1))

    print("Computing result for x=1 for the second time:")
    print(dummy_long_computation(1))

    print("Running actual benchmark on fibs")

    @cached
    def fibs_cached(x):
        if x == 0: return 0
        if x == 1: return 1
        return fibs_cached(x - 1) + fibs_cached(x - 2)

    def fibs_no_cache(x):
        if x == 0: return 0
        if x == 1: return 1
        return fibs_no_cache(x - 1) + fibs_no_cache(x - 2)

    print(inspect.getsource(fibs_cached))
    print(inspect.getsource(fibs_no_cache))

    print("Computing fibs for every in range 30-37 NO CACHE")
    ex_time = time.time()
    for i in range(30, 37):
        print(f"fibs({i}) = {fibs_no_cache(i)}")
    print(f"Execution took {time.time() - ex_time}")

    ex_time = time.time()
    print("Computing fibs for every in range 30-37 WITH CACHE")
    for i in range(30, 37):
        print(f"fibs({i}) = {fibs_cached(i)}")
    print(f"Execution took {time.time() - ex_time}")

    print("Benchmark finished")


if __name__ == "__main__":
    help_message = "Provide no args to run tests, --benchmark to run benchmark"
    bad_usage_message = "Bad usage, use -h"
    if len(sys.argv) > 2:
        print(bad_usage_message, file=sys.stderr)
        exit(1)
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == "-h":
            print(help_message)
            exit(0)
        elif arg == "--benchmark":
            run_benchmark()
            exit(0)
        else:
            print(bad_usage_message, file=sys.stderr)
            exit(1)
    else:
        unittest.main()
