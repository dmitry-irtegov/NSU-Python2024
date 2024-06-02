import pytest

from buckets import Buckets as OriginalBuckets
from fixed import FixedBuckets


@pytest.mark.parametrize("tested_class", [OriginalBuckets, FixedBuckets])
class TestBuckets:
    def test_constructor(self, tested_class):
        a = [1, 2, 3]
        b = tested_class(1, a)
        b.add(0, 8)
        assert b.find(0, 8)
        assert 8 not in a

    def test_add_find(self, tested_class):
        b = tested_class(2, [])
        assert not b.find(0, 10)
        assert not b.find(1, 10)
        b.add(0, 10)
        assert b.find(0, 10)
        assert not b.find(1, 10)

    def test_clear(self, tested_class):
        b = tested_class(1, [4])
        assert not b.find(0, 20)
        assert b.find(0, 4)
        b.add(0, 20)
        assert b.find(0, 20)
        assert b.find(0, 4)
        b.clear(0)
        assert not b.find(0, 20)
        assert b.find(0, 4)
