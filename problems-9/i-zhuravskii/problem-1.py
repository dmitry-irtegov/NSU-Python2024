import time
import unittest


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.perf_counter() - self.start_time
        if exc_type is not None:
            print(f"Timer has ended its work with ERROR\n"
                  f"Elapsed time = {self.elapsed_time} seconds\n")
            return
        print(f"Timer has ended its work SUCCESSFULLY\n"
              f"Elapsed time = {self.elapsed_time} seconds\n")

    def get_time(self):
        return self.elapsed_time


class TestTimer(unittest.TestCase):
    def test_standard(self):
        timer = Timer()
        with timer:
            time.sleep(4)

        self.assertGreaterEqual(timer.get_time() - 4.0)

    def test_with_error(self):
        with self.assertRaises(Exception):
            t = Timer()
            with t:
                time.sleep(4)
                raise Exception()

            self.assertGreaterEqual(t.get_time(), 4.0)
