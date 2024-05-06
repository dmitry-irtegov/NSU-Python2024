import unittest
import time

class Timer:
    enter_time: float | None
    exit_time: float | None

    def __init__(self) -> None:
        self.enter_time = None
        self.exit_time = None

    def __enter__(self):
        self.enter_time = time.time()
        
        return self

    def __exit__(self, type, value, traceback):
        self.exit_time = time.time()       

    def elapsed(self) -> float | None:
        """
        Returns `None` if called before entering context

        Returns time elapsed from entering context if called inside context

        Returns time spent inside context if called ouside of context
        """
        if self.enter_time is None:
            return None
        
        if self.exit_time is None:
            return time.time() - self.enter_time
        
        return self.exit_time - self.enter_time

SLEEP_DURATION = 1

def do_some_long_stuff():
    time.sleep(SLEEP_DURATION)

class TestTimer(unittest.TestCase):

    def test_inside_context(self):
        t0, t1, t2 = (0, 0, 0)

        with Timer() as t:
            t0 = t.elapsed()
            do_some_long_stuff()
            t1 = t.elapsed()
            do_some_long_stuff()
            t2 = t.elapsed()

        self.assertAlmostEqual(t0, 0, places=2)
        self.assertAlmostEqual(t1, SLEEP_DURATION, places=2)
        self.assertAlmostEqual(t2, 2 * SLEEP_DURATION, places=2)

    def test_outside_context(self):
        with Timer() as t:
            do_some_long_stuff()

        self.assertAlmostEqual(t.elapsed(), SLEEP_DURATION, places=2)

if __name__ == "__main__":
    unittest.main()
