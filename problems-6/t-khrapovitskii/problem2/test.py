from url_regex import find_urls


def get_parts(s: str) -> set[str]:
    parts_idx = find_urls(s)
    return set(map(lambda x: s[x[0]:x[1]], parts_idx))


class TestUrl:
    def test_empty(self):
        assert len(tuple(find_urls(""))) == 0

    def test_known_scheme(self):
        u1 = "https://localhost/123"
        s1 = f"some {u1}"
        assert get_parts(s1) == {u1}
        u2 = "HTTP://Problem"
        s2 = f"GET {u2} ="
        assert get_parts(s2) == {u2}
        s3 = "https:/nsu.qqqqq"
        assert get_parts(s3) == set()
        s4 = "htps://good.qqqqq"
        assert get_parts(s4) == set()

    def test_www(self):
        u1 = "www.nsu.qqqqq/123"
        s1 = f"some {u1}"
        assert get_parts(s1) == {u1}
        u2 = "wWw.nsu.qqqqq"
        s2 = f"GET {u2} ="
        assert get_parts(s2) == {u2}
        u3 = "www.bad"
        s3 = f"{u3}..ru"
        assert get_parts(s3) == {u3}

    def test_multiple(self):
        u1_1 = "https://google.com"
        u1_2 = "http://yandex.com"
        s1 = f"print {u1_1},{u1_2}"
        assert get_parts(s1) == {u1_1, u1_2}
