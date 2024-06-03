import math
import random
from typing import Callable


def gcd(a: int, b: int) -> int:
    power = 0
    while True:
        if a == 0:
            return b << power
        if b == 0:
            return a << power
        if a == 1 or b == 1:
            return 1 << power
        am = a % 2 == 0
        bm = b % 2 == 0
        if am and bm:
            power += 1
            a //= 2
            b //= 2
        elif am:
            a //= 2
        elif bm:
            b //= 2
        elif a > b:
            a = (a - b) // 2
        else:
            b = (b - a) // 2


def is_prime(n: int, a_list: list[int] | None = None) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if a_list is None:
        a_list = [random.randint(2, n - 2) for _ in range(4 * int(math.log2(n)))]
    t = n - 1
    s = 0
    while t % 2 == 0:
        s += 1
        t //= 2
    # random.seed(n)
    for a in a_list:
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        go_next = False
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                go_next = True
                break
        if go_next:
            continue
        return False
    return True


def divisor_cycle(x0: int, n: int, f: Callable[[int], int]) -> int:
    x = x0
    y = x0
    while True:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        if 1 < d:
            return d


def get_divisor(n: int) -> int:
    # n should be a composite number
    if n == 4:
        return 2
    for j in range(1, n - 2):
        for i in range(2, n):
            div = divisor_cycle(i, n, lambda val: (val ** 2 + j) % n)
            if div != n:
                return div
    return n


def factorize(n) -> dict[int, int]:
    if n < 2:
        return {}
    if is_prime(n):
        return {n: 1}
    d = get_divisor(n)
    if d == n:
        return {n: 1}
    if is_prime(d):
        i = 0
        while n % d == 0:
            n //= d
            i += 1
        base = {d: i}
    else:
        base = factorize(d)
        while n % d == 0:
            n //= d
    if n == 1:
        return base
    for k, v in factorize(n).items():
        base[k] = base.get(k, 0) + v
    return base


class Test:
    def test_gcd_trivial(self):
        assert gcd(0, 0) == 0
        assert gcd(0, 1) == 1
        assert gcd(0, 2) == 2
        assert gcd(0, 3) == 3
        assert gcd(1, 0) == 1
        assert gcd(2, 0) == 2
        assert gcd(3, 0) == 3
        assert gcd(1, 1) == 1
        assert gcd(1, 2) == 1
        assert gcd(1, 3) == 1
        assert gcd(2, 1) == 1
        assert gcd(3, 1) == 1

    def test_gdc_small(self):
        assert gcd(2, 5) == 1
        assert gcd(2, 6) == 2
        assert gcd(16, 32) == 16
        assert gcd(9, 15) == 3

    def test_gdc_big(self):
        assert gcd(13 * 7 * 5 * 2 ** 3 * 41, 7 * 5 ** 2 * 2 * 93) == 7 * 5 * 2

    def test_gdc_very_big(self):
        assert gcd(100000000069 * 41, 100000000069 * 1000000013681) == 100000000069

    def test_is_prime_small(self):
        assert is_prime(-3) is False
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(4) is False
        assert is_prime(5) is True

    def test_is_prime(self):
        assert is_prime(94) is False
        assert is_prime(97) is True

    def test_is_prime_big(self):
        assert is_prime(1000000013633) is True
        assert is_prime(1000009999 * 1000009831) is False

    def test_get_divisor(self):
        def check_composite(x):
            divisor = get_divisor(x)
            assert x % divisor == 0 and x != divisor and x != 1

        assert get_divisor(1) == 1
        check_composite(4)
        check_composite(6)
        check_composite(8)
        check_composite(9)
        check_composite(10)
        check_composite(12)
        check_composite(14)
        check_composite(1000009832)
        check_composite(1000009833)
        check_composite(1000009834)
        check_composite(1000009835)

    def test_factorize_trivial(self):
        assert factorize(-8) == {}
        assert factorize(0) == {}
        assert factorize(1) == {}
        assert factorize(2) == {2: 1}
        assert factorize(3) == {3: 1}

    def test_factorize(self):
        assert factorize(2) == {2: 1}
        assert factorize(10) == {2: 1, 5: 1}
        assert factorize(20) == {2: 2, 5: 1}
        assert factorize(120) == {2: 3, 5: 1, 3: 1}

    def test_factorize_big(self):
        assert factorize(151 * 179 * 179 * 251 * 683 * 683 * 683) == {151: 1, 179: 2, 251: 1, 683: 3}
        assert factorize(416833 * 417119 * 417133 * 417133) == {416833: 1, 417119: 1, 417133: 2}
        assert factorize(999961 * 999961 * 999983) == {999961: 2, 999983: 1}

    def test_factorize_very_big(self):
        assert factorize(2147481499518500483647) \
               == {2147483647: 1, 999999000001: 1}
        assert factorize(144483604528043653279487) \
               == {2147483647: 1, 67280421310721: 1}
        # assert factorize(67280354030366969700310721) \
        #        == {999999000001: 1, 67280421310721: 1}
        # this takes 16 sec
        # simple iterating from 0 to (not 999)999000001 with `pass` takes 26 sec
