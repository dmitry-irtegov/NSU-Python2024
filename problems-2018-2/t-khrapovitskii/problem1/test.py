from problem1 import is_complex


def test_digits():
    assert is_complex('0')
    assert is_complex('421')
    assert is_complex('-54')
    assert is_complex('1.86')


def test_bad():
    assert not is_complex('dsdf')
    assert not is_complex('1!')
    assert not is_complex('0-34')
    assert not is_complex('1/2')


def test_only_j():
    assert is_complex('j')
    assert is_complex('0j')
    assert is_complex('14.2j')
    assert is_complex('-100j')


def test_number_and_j():
    assert is_complex('54+j')
    assert is_complex('-1.1-0j')
    assert is_complex('10+14.2j')


def test_j_and_number():
    assert not is_complex('j+54')
    assert not is_complex('-0j-1.1')
    assert not is_complex('14.2j+10')


def test_char_replace():
    assert is_complex('45,1')
    assert is_complex('98i')
    assert is_complex('3-6I')
    assert not is_complex(' 10 +14 .2\n')
