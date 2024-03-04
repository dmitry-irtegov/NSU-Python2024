#!/usr/bin/env python3
import time

class Timer:
    def __init__(self, block_name=None):
        if not block_name is None and not isinstance(block_name, str):
            raise TypeError("block_name can be only None or str type")
        self.block_name = block_name

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exception_type, exception_value, traceback):
        elapsed = time.perf_counter() - self.start
        if self.block_name is None:
            print(f'Time elapsed: {elapsed} s')
        else:
            print(f'Time elapsed in block \'{self.block_name}\': {elapsed} s')

if __name__ == "__main__":
    with Timer():
        time.sleep(1)

    with Timer('some name'):
        time.sleep(1)

    with Timer('with exception'):
        raise RuntimeError()
