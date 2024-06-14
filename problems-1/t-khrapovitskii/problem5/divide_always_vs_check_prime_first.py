import contextlib
import resource
import time

from problem5 import is_prime

start = 982300000
end = 982451653

number = 170141183460469231731687303715884105727


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


if __name__ == '__main__':
    x = []
    with Timer("Simple"):
        for i in range(start, end + 1):
            x.append(number % i)

    y = []
    with Timer("Smart"):
        for i in range(start, end + 1):
            if is_prime(i):
                y.append(number % i)

    print(len(x), len(y))
