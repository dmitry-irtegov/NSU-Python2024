import re
import unittest


def find_urls(text: str) -> list:
    url_pattern = re.compile(r'\b(?:https?://|www\.|https?://www\.)\w+\.\w{2,3}(?:/\w+|)*\b')
    urls = url_pattern.findall(text)
    return urls


class FindUrlsTest(unittest.TestCase):
    def test_find_urls(self):
        self.assertEqual(["www.example.com"],
                         find_urls("www.example.com is a link, example.org is not a link"))
        self.assertEqual(["http://example.com"],
                         find_urls("link: http://example.com"))
        self.assertEqual(["https://yandex.ru"],
                         find_urls("link: https://yandex.ru"))
        self.assertEqual(["https://www.google.com"],
                         find_urls("link: https://www.google.com "))

        # По заданию нужно определять только по префиксам "https" и "www"
        self.assertEqual([],
                         find_urls("https://ru.wikipedia.org"))
        self.assertEqual([],
                         find_urls("ru.wikipedia.org"))

        self.assertEqual(["https://www.wikipedia.org/wiki"],
                         find_urls("https://www.wikipedia.org/wiki"))
        self.assertEqual(["www.wikipedia.org/wiki"],
                         find_urls("www.wikipedia.org/wiki"))

        self.assertEqual(["https://www.wikipedia.org/wiki/Philosophy"],
                         find_urls("https://www.wikipedia.org/wiki/Philosophy"))
        self.assertEqual(["www.wikipedia.org/wiki/Philosophy"],
                         find_urls("www.wikipedia.org/wiki/Philosophy"))


if __name__ == '__main__':
    unittest.main()
