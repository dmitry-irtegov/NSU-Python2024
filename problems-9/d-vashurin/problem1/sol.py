import time
from typing import Any, Literal, cast


class Timer:
    __slots__ = ("_start", "_end")

    def __init__(self) -> None:
        self._start: int | None = None
        self._end: int | None = None

    def __enter__(self) -> None:
        self._start = time.perf_counter_ns()
        self._end = None

    def __exit__(self, *exc: Any) -> Literal[False]:
        self._end = time.perf_counter_ns()
        return False

    async def __aenter__(self) -> None:
        return self.__enter__()

    async def __aexit__(self, *exc: Any) -> Literal[False]:
        return self.__exit__(*exc)

    @property
    def is_running(self) -> bool:
        return self._start is not None and self._end is None

    @property
    def elapsed(self) -> int:
        if self._end is None:
            return time.perf_counter_ns() - cast(int, self._start)

        return self._end - cast(int, self._start)
