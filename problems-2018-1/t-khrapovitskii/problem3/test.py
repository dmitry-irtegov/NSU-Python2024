import pytest
from list_sieve import ListSieve
from set_add_sieve import SetAddSieve
from set_remove_sieve import SetRemoveSieve
from bitarray_sieve import BitArraySieve
from eratosphenes import eratosthenes


@pytest.mark.parametrize("sieve_class", [ListSieve, SetAddSieve, SetRemoveSieve, BitArraySieve])
class TestProblem3:
    def test_nothing(self, sieve_class):
        sieve = sieve_class(2)
        eratosthenes(sieve, 2)
        assert not sieve.is_known_composite(2)
        assert set(sieve.get_primes()) == {2}

    def test_small(self, sieve_class):
        sieve = sieve_class(20)
        eratosthenes(sieve, 20)
        assert set(sieve.get_primes()) == {2, 3, 5, 7, 11, 13, 17, 19}

    def test_big(self, sieve_class):
        n = 1000000
        sieve = sieve_class(n)
        eratosthenes(sieve, n)
        assert not sieve.is_known_composite(941683)
        assert sieve.is_known_composite(941697)
        assert not sieve.is_known_composite(941701)

    # def test_large(self, sieve_class):
    #     n = 100000000
    #     sieve = sieve_class(n)
    #     eratosthenes(sieve, n)
    #     assert not sieve.is_known_composite(941683)
    #     assert sieve.is_known_composite(941697)
    #     assert not sieve.is_known_composite(941701)
