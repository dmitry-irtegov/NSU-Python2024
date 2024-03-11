import time
from typing import Any


class Timer:
    __slots__ = ("_start")

    def __enter__(self) -> None:
        self._start = time.perf_counter_ns()

    def __exit__(self, *exc: Any) -> None:
        if exc[0] is None:
            print(time.perf_counter_ns() - self._start)
