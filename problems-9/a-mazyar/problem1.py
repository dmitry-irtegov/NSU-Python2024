from time import perf_counter, sleep
import unittest

class Timer:
    def __enter__(self):
        self._start_time = perf_counter()
        self._finished = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end_time = perf_counter()
        self._finished = True
        print(f"Contex exited with elapsed time: {self.elapsed}")

    @property
    def elapsed(self):
        if self._finished:
            return self._end_time - self._start_time
        return perf_counter() - self._start_time
    

class TimerTest(unittest.TestCase):
    def test_normal_exit(self):
        timer = Timer()
        with timer:
            sleep(1)
        
        self.assertGreaterEqual(timer.elapsed, 1.0)

    def test_exception_exit(self):
        with self.assertRaises(RuntimeError):
            timer = Timer()
            with timer:
                sleep(1)
                raise RuntimeError("Ugly error")
        
        self.assertGreaterEqual(timer.elapsed, 1.0)

if __name__ == '__main__':
    unittest.main()