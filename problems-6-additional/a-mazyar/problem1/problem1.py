from time import sleep, perf_counter
import unittest

class FastHashCol(list):
    """ This class overrides hash to calculate it just once.
    @cached will use is as a key to look up cached values.
    """
    def __init__(self, hashable_col):
        self[:] = hashable_col
        self.hashvalue = hash(hashable_col)

    def __hash__(self):
        return self.hashvalue
    
_kwd_mark = (object(), )
def get_args_col(args, kwargs, typed, 
                 fast_hash=True):
    """ Returns a collection that represents all the arguments.
    This collection will be used as a key in cache.
    """
    col = args
    if kwargs:
        col += _kwd_mark
        for kwarg in kwargs.items():
            col += (kwarg, )
    if typed:
        col += tuple(type(arg) for arg in args)
        if kwargs:
            col += tuple(type(kwarg) for kwarg in kwargs)
    
    if fast_hash:
        return FastHashCol(col)
    return col

def cached(typed=False, fast_hash=True):
    def decorator(func):
        cache = {}
        def cached_func(*args, **kwargs):
            key = get_args_col(args, kwargs, typed, fast_hash)
            if key in cache:
                return cache[key]
            else:
                value = func(*args, **kwargs)
                cache[key] = value
                return value
        return cached_func
    return decorator

class MyCacheTest(unittest.TestCase):
    def test_cache_time(self):
        @cached()
        def sleep_add(arg1, arg2,):
            sleep(2)
            return arg1 + arg2
        
        start_init_calc = perf_counter()
        res = sleep_add(2, 1)
        end_init_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_init_calc - start_init_calc, 2.0)

        start_cached = perf_counter()
        res = sleep_add(2, 1)
        end_cached = perf_counter()
        self.assertEqual(res, 3)
        self.assertLess(end_cached - start_cached, 2.0)
        
    def test_kwarg_order(self):
        @cached()
        def sleep_add(arg1, arg2):
            sleep(2)
            return arg1 + arg2
        
        start_calc = perf_counter()
        res = sleep_add(arg1=2, arg2=1)
        end_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_calc - start_calc, 2.0)

        start_reverse_calc = perf_counter()
        res = sleep_add(arg2=1, arg1=2)
        end_reverse_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_reverse_calc - start_reverse_calc, 2.0)

        start_cached = perf_counter()
        res = sleep_add(arg1=2, arg2=1)
        end_cached = perf_counter()
        self.assertEqual(res, 3)
        self.assertLessEqual(end_cached - start_cached, 2.0)

    def test_typed_cache(self):
        @cached(typed=True)
        def sleep_add(arg1, arg2):
            sleep(2)
            return arg1 + arg2
        
        start_int_calc = perf_counter()
        res = sleep_add(2, 1)
        end_int_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_int_calc - start_int_calc, 2.0)

        start_float_calc = perf_counter()
        res = sleep_add(2.0, 1.0)
        end_float_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_float_calc - start_float_calc, 2.0)

        start_cached = perf_counter()
        res = sleep_add(int(2), int(1))
        end_cached = perf_counter()
        self.assertEqual(res, 3)
        self.assertLessEqual(end_cached - start_cached, 2.0)

    def test_slow_hash(self):
        @cached(fast_hash=False)
        def sleep_add(arg1, arg2):
            sleep(2)
            return arg1 + arg2
        
        start_init_calc = perf_counter()
        res = sleep_add(2, 1)
        end_init_calc = perf_counter()
        self.assertEqual(res, 3)
        self.assertGreaterEqual(end_init_calc - start_init_calc, 2.0)

        start_cached = perf_counter()
        res = sleep_add(2, 1)
        end_cached = perf_counter()
        self.assertEqual(res, 3)
        self.assertLess(end_cached - start_cached, 2.0)
    
    def test_kwarg_hack(self):
        @cached()
        def my_add(arg1, arg2):
            return arg1 + arg2
        
        my_add((1,), arg2=(2,))
        hacked_cache_res = my_add((1,), ('arg2', (2, )))
        self.assertEqual(hacked_cache_res, (1, 'arg2', (2, )))


def time_fast_hash():
    print("Measuring FastHashCol impact")
    big_arg1 = tuple(i for i in range(1000000))
    big_arg2 = tuple(i for i in range(1000000, 2000000))

    print("Without FastHashCol")
    @cached(typed=True, fast_hash=False)
    def my_add(arg1, arg2):
        return arg1 + arg2
    
    my_add(big_arg1, big_arg2)
    start_slow_hash = perf_counter()
    my_add(big_arg1, big_arg2)
    my_add(big_arg1, big_arg2)
    my_add(big_arg1, big_arg2)
    end_slow_hash = perf_counter()
    print("\tTime:", end_slow_hash-start_slow_hash)

    print("With FastHashCol")
    @cached(typed=True, fast_hash=True)
    def my_add(arg1, arg2):
        return arg1 + arg2
    
    my_add(big_arg1, big_arg2)
    start_fast_hash = perf_counter()
    my_add(big_arg1, big_arg2)
    my_add(big_arg1, big_arg2)
    my_add(big_arg1, big_arg2)
    end_fast_hash = perf_counter()
    print("\tTime:", end_fast_hash-start_fast_hash)

if __name__ == "__main__":
    time_fast_hash()
    unittest.main()