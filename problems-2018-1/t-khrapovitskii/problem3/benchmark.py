import gc
import os
import time
from typing import Type

import psutil

from bitarray_sieve import BitArraySieve
from eratosphenes import eratosthenes
from list_sieve import ListSieve
from set_add_sieve import SetAddSieve
from set_remove_sieve import SetRemoveSieve
from sieve import Sieve

# import tracemalloc

N = 100000000

process = psutil.Process(os.getpid())
last_time = 0.
total_time = 0.


def get_memory() -> str:
    mem = process.memory_info().vms
    return f"{mem // 1024 // 1024}M"


def get_time_delta() -> float:
    global last_time
    global total_time
    delta = time.time() - last_time
    last_time = time.time()
    total_time += delta
    return delta


if __name__ == '__main__':
    sieve_classes: list[Type[Sieve]] = [ListSieve, SetAddSieve, SetRemoveSieve, BitArraySieve]
    for sieve_class in sieve_classes:
        gc.collect()
        print(sieve_class.__name__)
        print("Memory usage before:", get_memory())
        last_time = time.time()
        total_time = 0
        # noinspection PyRedeclaration
        sieve = sieve_class.create(N)
        print(f"Initializing object: {get_time_delta():.3f}s, memory after: {get_memory()}")
        eratosthenes(sieve, N)
        print(f"Running algorithm: {get_time_delta():.3f}s, memory after: {get_memory()}")
        result = sieve.get_primes()
        print(f"Getting primes as a Sequence: {get_time_delta():.3f}s, memory after: {get_memory()}")
        print(f"Total time: {total_time:.3f}s")
        del sieve
        del result
        print()
