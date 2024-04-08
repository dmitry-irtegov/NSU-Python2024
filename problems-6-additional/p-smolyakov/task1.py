#!/usr/bin/env python3
import time
import unittest
from copy import deepcopy

def cached(func):
    func_dict = {}

    def wrapper(*args, **kwargs):
        kwargs_tuple = tuple(sorted(kwargs.items(), key = lambda pair: pair[0]))
        args_entry = tuple([args, kwargs_tuple])

        if args_entry not in func_dict:
            try:
                func_dict[args_entry] = ('retval', func(*args, **kwargs))
            except BaseException as e:
                func_dict[args_entry] = ('exception', e)

        variant, result = func_dict[args_entry]
        if variant == 'retval':
            return result
        else:
            raise deepcopy(result).with_traceback(result.__traceback__)

    return wrapper



class TranslatorTests(unittest.TestCase):
    def test_simple(self):
        @cached
        def _long_sum(a, b = 0):
            time.sleep(2)
            return a + b

        start = time.perf_counter()
        res = _long_sum(1)
        end = time.perf_counter()

        self.assertTrue(end - start >= 2.0)
        self.assertEqual(res, 1)


        start = time.perf_counter()
        res = _long_sum(1)
        end = time.perf_counter()

        self.assertTrue(end - start < 2.0)
        self.assertEqual(res, 1)

    
    def test_different_args(self):
        @cached
        def _long_sum(a, b = 0):
            time.sleep(2)
            return a + b

        start = time.perf_counter()
        res = _long_sum(1)
        end = time.perf_counter()

        self.assertTrue(end - start >= 2.0)
        self.assertEqual(res, 1)


        start = time.perf_counter()
        res = _long_sum(1, 0)
        end = time.perf_counter()

        self.assertTrue(end - start >= 2.0)
        self.assertEqual(res, 1)


        start = time.perf_counter()
        res = _long_sum(1, b = 0)
        end = time.perf_counter()

        self.assertTrue(end - start >= 2.0)
        self.assertEqual(res, 1)


        start = time.perf_counter()
        res = _long_sum(2)
        end = time.perf_counter()

        self.assertTrue(end - start >= 2.0)
        self.assertEqual(res, 2)


    def test_exception(self):
        @cached
        def _with_exception():
            time.sleep(2)
            raise RuntimeError('error occured after 2 secs of execution')

        start = time.perf_counter()
        with self.assertRaises(RuntimeError):
            _with_exception()
        end = time.perf_counter()
        self.assertTrue(end - start >= 2.0)

        start = time.perf_counter()
        with self.assertRaises(RuntimeError):
            _with_exception()
        end = time.perf_counter()
        self.assertTrue(end - start < 2.0)
        


if __name__ == "__main__":
    unittest.main()
