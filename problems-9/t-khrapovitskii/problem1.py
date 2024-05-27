import random
import time
import resource
import contextlib
import unittest
from io import StringIO
from unittest.mock import patch
import re


class Timer(contextlib.AbstractContextManager):
    def __init__(self, message=''):
        self.message = message

    def __enter__(self):
        self.enter_time = time.time()
        self.enter_res = resource.getrusage(resource.RUSAGE_SELF)

    def __exit__(self, exc_type, exc_val, exc_tb):
        exit_time = time.time()
        exit_res = resource.getrusage(resource.RUSAGE_SELF)
        print(self.message)
        print(f'real    {self.format_time(exit_time - self.enter_time)}')
        print(f'user    {self.format_time(exit_res.ru_utime - self.enter_res.ru_utime)}')
        print(f'sys     {self.format_time(exit_res.ru_stime - self.enter_res.ru_stime)}')

    @staticmethod
    def format_time(seconds: float) -> str:
        m = int(seconds) // 60
        s = seconds - m * 60
        return f'{m}m{s:.3f}s'


def bogosort(a: list):
    bad_shuffles = []
    while True:
        random.shuffle(a)
        is_sorted = True
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                bad_shuffles.append(a[:i])
                is_sorted = False
                break
        if is_sorted:
            return


if __name__ == '__main__':
    with Timer():
        bogosort([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


class Test(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_only_arithmetic(self, mock_stdout: StringIO):
        with Timer():
            _ = 0
            for _ in range(1000000):
                _ = (_ + 1) % 2
        out = mock_stdout.getvalue()
        match = re.match(r"\nreal\s+0m([\d.]+)s\nuser\s+0m([\d.]+)s\nsys\s+0m([\d.]+)s\n$", out)
        assert match is not None
        assert float(match[1]) > 0
        assert float(match[2]) > 0
        assert float(match[3]) < float(match[1]) / 100

    @patch('sys.stdout', new_callable=StringIO)
    def test_sleep(self, mock_stdout: StringIO):
        with Timer():
            time.sleep(2)
        out = mock_stdout.getvalue()
        match = re.match(r"\nreal\s+0m([\d.]+)s\nuser\s+0m([\d.]+)s\nsys\s+0m([\d.]+)s\n$", out)
        assert match is not None
        assert float(match[1]) >= 2
        assert float(match[1]) < 2.1

    @patch('sys.stdout', new_callable=StringIO)
    def test_sys_memory_alloc(self, mock_stdout: StringIO):
        with Timer():
            bogosort([1, 2, 3, 4, 5, 6, 7, 8, 0])
        out = mock_stdout.getvalue()
        match = re.match(r"\nreal\s+0m([\d.]+)s\nuser\s+0m([\d.]+)s\nsys\s+0m([\d.]+)s\n$", out)
        assert match is not None
        assert float(match[3]) > 0
