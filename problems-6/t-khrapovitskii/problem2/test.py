from url_regex import find_urls


def compare_iterables(iterable1, iterable2):
    for a, b in zip(iterable1, iterable2, strict=True):
        assert a == b


class TestUrl:
    def test_empty(self):
        assert len(tuple(find_urls(""))) == 0

    def test_known_scheme(self):
        s1 = "some https://localhost/123"
        s2 = "GET HTTP://Problem ="
        s3 = "https:/nsu.qqqqq"
        s4 = "htps://good.qqqqq"
        compare_iterables(find_urls(s1), [(5, len(s1))])
        compare_iterables(find_urls(s2), [(4, len(s2) - 2)])
        compare_iterables(find_urls(s3), [])
        compare_iterables(find_urls(s4), [])

    def test_www(self):
        s1 = "some www.nsu.qqqqq/123"
        s2 = "GET wWw.nsu.qqqqq ="
        s3 = "www.bad..ru"
        compare_iterables(find_urls(s1), [(5, len(s1))])
        compare_iterables(find_urls(s2), [(4, len(s2) - 2)])
        compare_iterables(find_urls(s3), [(0, len(s3) - 4)])

    def test_known_domain(self):
        s1 = "\"site.ru\""
        s2 = "GET ietf.org/rfc/rfc3986.txt ="
        s3 = "GET ietf.gororg/rfc/rfc3986.txt ="
        compare_iterables(find_urls(s1), [(1, len(s1) - 1)])
        compare_iterables(find_urls(s2), [(4, len(s2) - 2)])
        compare_iterables(find_urls(s3), [])

    def test_multiple(self):
        s1 = "print http://google.com,http://yandex.com"
        compare_iterables(find_urls(s1), [(6, 23), (24, 41)])
