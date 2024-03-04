#!/usr/bin/env python3
import time

class Timer:
    def __init__(self, block_name=None):
        if block_name is not None and not isinstance(block_name, str):
            raise TypeError('block_name can be only None or str type')
        self.__block_name = block_name

    def __enter__(self):
        self.__start = time.perf_counter()

    def __exit__(self, exception_type, exception_value, traceback):
        elapsed = time.perf_counter() - self.__start
        if self.__block_name is None:
            print(f'Time elapsed: {elapsed} s')
        else:
            print(f'Time elapsed in block \'{self.__block_name}\': {elapsed} s')

if __name__ == '__main__':
    with Timer():
        time.sleep(1)

    with Timer('some name'):
        time.sleep(1)

    with Timer('with exception'):
        raise RuntimeError()
