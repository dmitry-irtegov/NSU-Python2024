from sol import shuffle, sort_alphabetically, replace_algorithm


def test_random() -> None:
    assert shuffle("") == ""
    
    word = shuffle("Word")
    assert word[0] == "W"
    assert word[-1] == "d"


def test_alphabet() -> None:
    assert sort_alphabetically("World") == "Wlord"


def test_replace_alphabet() -> None:
    assert replace_algorithm(
        "The quick brown fox jumps over the lazy dog", sort_alphabetically,
    ) == "The qciuk borwn fox jmpus oevr the lazy dog"


def test_replace_id() -> None:
    assert replace_algorithm(
        "The quick brown fox jumps over the lazy dog", lambda x: x,
    ) == "The quick brown fox jumps over the lazy dog"
