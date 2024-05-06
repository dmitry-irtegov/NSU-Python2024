import time
import unittest


class Timer(object):

    def __enter__(self):
        self._time_delta = 0
        self._start_time = time.perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._time_delta = time.perf_counter() - self._start_time
        print(f'Took time: {self._time_delta} seconds')

    def get_execution_time(self):
        if self._time_delta > 0:
            return self._time_delta
        return time.perf_counter() - self._start_time


class TimerTest(unittest.TestCase):
    def test_timer(self):
        t = Timer()
        with t:
            time.sleep(3)
        self.assertGreaterEqual(t.get_execution_time(), 3.0)

    def test_time_after(self):
        with self.assertRaises(RuntimeError):
            timer = Timer()
            with timer:
                time.sleep(1)
                raise RuntimeError("Some exception")
        self.assertGreaterEqual(timer.get_execution_time(), 1.0)


if __name__ == '__main__':
    unittest.main()
