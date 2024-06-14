from io import StringIO
from sol import read_thesaurus, reverse, write_thesaurus

INITIAL = {
    "punishment": ["malum", "multa"],
    "apple": ["malum", "pomum", "popula"],
    "fruit": ["baca", "bacca", "popum"],
}
REVERSED = {
    "baca": ["fruit"],
    "bacca": ["fruit"],
    "malum": ["apple", "punishment"],
    "multa": ["punishment"],
    "pomum": ["apple"],
    "popula": ["apple"],
    "popum": ["fruit"],
}


def test_read():
    with StringIO() as io:
        for string in [
            "punishment - malum, multa",
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
        ]:
            io.write(string)
            io.write("\n")

        io.seek(0)

        assert read_thesaurus(io) == INITIAL


def test_reverse():
    assert reverse(INITIAL) == REVERSED


def test_idempotency():
    assert reverse(reverse(INITIAL)) == INITIAL
    assert reverse(reverse(REVERSED)) == REVERSED


def test_write():
    with StringIO() as io:
        write_thesaurus(io, INITIAL)

        assert io.getvalue() == (
            "apple - malum, pomum, popula\n"
            "fruit - baca, bacca, popum\n"
            "punishment - malum, multa\n"
        )
