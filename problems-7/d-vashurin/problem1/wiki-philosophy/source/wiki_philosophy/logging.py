from collections.abc import Mapping
from logging import Formatter
from types import TracebackType
from typing import Any, Literal


class ExcFormatter(Formatter):
    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal['%'] | Literal['{'] | Literal['$'] = "%",
        validate: bool = True,
        *,
        defaults: Mapping[str, Any] | None = None,
        exc_info: bool = False
    ) -> None:
        super().__init__(fmt, datefmt, style, validate, defaults=defaults)

        self._exc_info = exc_info

    def formatException(
        self,
        ei: tuple[
            type[BaseException], BaseException, TracebackType | None
        ] | tuple[None, None, None],
    ) -> str:
        if not self._exc_info:
            return ""

        return super().formatException(ei)
