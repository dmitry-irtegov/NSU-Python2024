import sys
import time
import unittest


class Timer:
    def __enter__(self):
        self._start = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._value = time.perf_counter() - self._start
        if exc_type is not None:
            print(f"TIMER (Error): Elapsed time = {self._value} seconds\n", file=sys.stderr)
            return
        print(f"TIMER (Success): Elapsed time = {self._value} seconds")

    def get_value(self):
        return self._value

#
class TestTimer(unittest.TestCase):
    def test_basic(self):
        t = Timer()
        with t:
            time.sleep(2)

        self.assertGreaterEqual(t.get_value(), 2.0)

    def test_with_error(self):
        with self.assertRaises(Exception):
            t = Timer()
            with t:
                time.sleep(2)
                raise Exception()

            self.assertGreaterEqual(t.get_value(), 2.0)
