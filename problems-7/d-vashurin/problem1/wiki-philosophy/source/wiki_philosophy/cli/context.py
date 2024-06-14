__all__ = (
    "AppContext",
)

import logging
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from collections.abc import MutableMapping
from contextlib import AbstractContextManager, ExitStack
from dbm import dumb as dbm
from pathlib import Path
from tempfile import TemporaryDirectory
from types import TracebackType
from typing import Any, Self, cast

from wiki_philosophy.consts import RANDOM_ARTICLE

logger = logging.getLogger(__name__)


def provide_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="wiki-philosophy",
        description="jump on Wikipedia links until you find an article about philosophy",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "article",
        nargs="?",
        default=RANDOM_ARTICLE,
        help="initial article",
    )

    parser.add_argument(
        "-c", "--cache",
        nargs="?",
        help="cache database location (requires two files: CACHE.dat and CACHE.dir)",
    )

    return parser


class AppContext(AbstractContextManager):
    def __init__(
        self,
        database: MutableMapping[str, bytes],
        initial_aritcle: str,
        stack: AbstractContextManager[Any],
    ) -> None:
        self._database = database
        self._initial_aritcle = initial_aritcle
        self._stack = stack

    @property
    def database(self) -> MutableMapping[str, bytes]:
        return self._database

    @property
    def initial_article(self) -> str:
        return self._initial_aritcle

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        return self._stack.__exit__(exc_type, exc_value, traceback)

    @classmethod
    def provide(cls) -> Self:
        args = provide_parser().parse_args()
        stack = ExitStack()

        if args.cache is None:
            try:
                temp_dir = stack.enter_context(TemporaryDirectory(ignore_cleanup_errors=True))
            except OSError as exc:
                logger.exception(
                    "failed to create a temporary directory, reason - %s", exc.strerror
                )
                raise exc
            logger.debug("created a temporary directory for the cache database at '%s'", temp_dir)
            args.cache = Path(temp_dir) / "cache-db"

        try:
            db = stack.enter_context(dbm.open(args.cache, "c"))
        except OSError as exc:
            logger.exception("failed to open the cache database, reason - %s", exc.strerror)
            raise exc
        logger.debug("opened the cache database at '%s'", args.cache)

        return cls(cast(MutableMapping[str, bytes], db), args.article, stack)
