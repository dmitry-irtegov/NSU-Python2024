from asyncio import sleep as asleep
from time import sleep

import pytest

from sol import Timer

ACCEPTABLE_DELTA_NS = 50_000_000


@pytest.fixture
def timer() -> Timer:
    return Timer()


def assert_elapsed_ns(measured: int, expected: int) -> None:
    assert abs(measured - expected) <= ACCEPTABLE_DELTA_NS


def test_sync_simple(timer: Timer) -> None:
    with timer:
        sleep(1)

    assert_elapsed_ns(timer.elapsed, 1_000_000_000)


def test_sync_running(timer: Timer) -> None:
    with timer:
        sleep(1)

        assert_elapsed_ns(timer.elapsed, 1_000_000_000)
        assert timer.is_running

        sleep(0.5)

    assert_elapsed_ns(timer.elapsed, 1_500_000_000)


def test_not_swallows_exceptions(timer: Timer) -> None:
    with pytest.raises(RuntimeError), timer:
        sleep(1)

        assert timer.is_running

        message = "A fancy exception!"
        raise RuntimeError(message)

    assert not timer.is_running
    sleep(1)
    assert_elapsed_ns(timer.elapsed, 1_000_000_000)


@pytest.mark.asyncio
async def test_async_simple(timer: Timer) -> None:
    async with timer:
        await asleep(1)

    assert_elapsed_ns(timer.elapsed, 1_000_000_000)


@pytest.mark.asyncio
async def test_async_running(timer: Timer) -> None:
    async with timer:
        await asleep(1)

        assert_elapsed_ns(timer.elapsed, 1_000_000_000)
        assert timer.is_running

        await asleep(0.5)

    assert_elapsed_ns(timer.elapsed, 1_500_000_000)
