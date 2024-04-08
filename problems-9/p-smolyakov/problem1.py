#!/usr/bin/env python3
import time
import unittest

class Timer:
    def __enter__(self):
        self.__running = True
        self.__start = time.perf_counter()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.__running = False
        self.__end = time.perf_counter()

    def is_running(self):
        return self.__running

    def value(self):
        if not self.__running:
            return self.__end - self.__start
        else:
            return time.perf_counter() - self.__start

    def __str__(self):
        return f'TIMER INFO\n---\nTimer running: {self.__running}\nTime is {self.value()} sec\n'
        

class TimerTest(unittest.TestCase):
    def test_simple(self):
        with Timer() as t:
            time.sleep(1)

        self.assertTrue(t.value() >= 1.0)
        self.assertFalse(t.is_running())


    def test_measuring_inside(self):
        with Timer() as t:
            time.sleep(1)

            self.assertTrue(t.is_running())
            self.assertTrue(t.value() >= 1.0)

            time.sleep(1)

        self.assertTrue(t.value() >= 2.0)
        self.assertFalse(t.is_running())


    def test_with_exception(self):
        with self.assertRaises(RuntimeError):
            with Timer() as t:
                time.sleep(1)
                raise RuntimeError("aoaoa")

        self.assertTrue(t.value() >= 1.0)
        self.assertFalse(t.is_running())


if __name__ == '__main__':
    unittest.main()
