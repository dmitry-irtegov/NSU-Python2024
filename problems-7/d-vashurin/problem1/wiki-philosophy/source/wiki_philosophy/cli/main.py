__all__ = (
    "entrypoint",
)

import importlib
import importlib.resources
import logging
import logging.config
import tomllib
from collections.abc import MutableMapping
from typing import cast

import requests
from bs4 import BeautifulSoup

from wiki_philosophy import resources
from wiki_philosophy.cli.context import AppContext
from wiki_philosophy.consts import (
    INTERNAL_LINK_PREFIX,
    PHILOSOPHY_ARTICLE,
    RANDOM_ARTICLE,
    REQUESTS_PER_SECOND,
)
from wiki_philosophy.parse import find_normal_link, to_article, to_link
from wiki_philosophy.throttle import Throttler
from wiki_philosophy.types import ReturnCode

logger = logging.getLogger(__name__)


def main(database: MutableMapping[str, bytes], article: str) -> ReturnCode:
    throttler = Throttler(REQUESTS_PER_SECOND)

    if article == RANDOM_ARTICLE:
        logger.info("picking a random article...")

        with throttler:
            try:
                response = requests.get(to_link(article), allow_redirects=False)
                response.raise_for_status()
            except requests.RequestException as exc:
                logger.exception("failed to pick an article, reason - %s", exc)
                return ReturnCode.NETWORK_FAILURE

        if "Location" not in response.headers:
            logger.error("Wikipeda hasn't provided a random article :(")
            return ReturnCode.MISSING_RANDOM

        article = response.headers["Location"].removeprefix(INTERNAL_LINK_PREFIX)
        logger.info("picked: %s", article)
    else:
        logger.info("starting with: %s", article)

    visited = set[str]()
    while article not in visited and article != PHILOSOPHY_ARTICLE:
        visited.add(article)

        try:
            next_article: str | bytes | None = database.get(article)
        except KeyError as exc:
            logger.exception("failed to check if the cache contains '%s', reason - %", exc)
            return ReturnCode.INVALID_KEY

        if next_article is not None:
            article = cast(bytes, next_article).decode()
            logger.info("got next article from cache: %s", article)
            continue

        with throttler:
            logger.debug("retrieving: %s", article)
            response = requests.get(to_link(article))
            response.raise_for_status()

        link = find_normal_link(BeautifulSoup(response.content, "html.parser"))
        if link is None:
            logger.info("encountered a dead end")
            return ReturnCode.SUCCESS

        next_article = to_article(link)
        logger.info("parsed next article: %s", next_article)
        database[article] = next_article.encode()
        article = next_article

    if article in visited:
        logger.info("encountered a loop on: %s", article)

    if article == PHILOSOPHY_ARTICLE:
        logger.info("found the philosophy!")

    return ReturnCode.SUCCESS


def bootstrap() -> None:
    app_logging_config = importlib.resources.files(resources) / "app_logging.toml"
    with app_logging_config.open("rb") as stream:
        logging.config.dictConfig(tomllib.load(stream))

    try:
        ctx = AppContext.provide()
    except Exception:
        exit(ReturnCode.BOOTSTRAP_FAILURE)

    try:
        with ctx:
            code = main(ctx.database, ctx.initial_article)
    except requests.RequestException as exc:
        url = exc.request.url if exc.request else "<unknown-url>"
        logger.exception(
            "failed to GET a Wikipedia article at '%s', reason - %s", url, exc
        )
        exit(1)
    except Exception as exc:
        logger.exception("unknown exception happened, reason - %s", exc)
        exit(1)
    else:
        quit(code)


def entrypoint() -> None:
    try:
        bootstrap()
    except KeyboardInterrupt:
        logger.info("captured Ctrl + C, exiting...")
