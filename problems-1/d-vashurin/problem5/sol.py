from math import sqrt


def factorize(number: int) -> list[tuple[int, int]]:
    if number < 2:
        return []

    factors: list[tuple[int, int]] = []
    for factor in range(2, int(sqrt(number)) + 1):
        power = 0
        factorized, remainder = divmod(number, factor)
        while remainder == 0 and factorized > 0:
            power += 1
            number = factorized
            factorized, remainder = divmod(number, factor)

        if power != 0:
            factors.append((factor, power))
            if number == 1:
                return factors

    if number != 1:
        factors.append((number, 1))

    return factors
