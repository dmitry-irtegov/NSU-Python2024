def collaz(number: int) -> list[int]:
    seq = [ number ]

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        seq.append(number)

    return seq

def print_collaz_seq(seq: list[int]):
    print(" -> ".join([ str(x) for x in seq ]))

if __name__ == "__main__":
    print_collaz_seq(collaz(1))
    print_collaz_seq(collaz(2))
    print_collaz_seq(collaz(3))
    print_collaz_seq(collaz(15))