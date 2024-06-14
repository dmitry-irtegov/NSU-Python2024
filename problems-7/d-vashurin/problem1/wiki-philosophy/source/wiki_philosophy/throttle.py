import logging
import time
from contextlib import AbstractContextManager
from types import TracebackType

logger = logging.getLogger(__name__)


class Throttler(AbstractContextManager[None]):
    def __init__(self, rps: float) -> None:
        self._window = 1 / rps
        self._last_called = 0.0

    def __enter__(self) -> None:
        delta = time.perf_counter() - self._last_called
        if delta < self._window:
            sleep_duration = self._window - delta
            logger.debug("throttling; sleep for {:3f}", sleep_duration)
            time.sleep(sleep_duration)

        self._last_called = time.perf_counter()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        return None
