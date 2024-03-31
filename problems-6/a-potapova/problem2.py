import re
import unittest


def find_urls(text: str) -> list:
    url_pattern = re.compile(r'\b(?:https?://|www\.|https?://www\.)\w+\.\w{2,3}(?:/\w+|)*\b')
    urls = url_pattern.findall(text)
    return urls


class FindUrlsTest(unittest.TestCase):
    def test_find_urls_with_http_https_prefix(self):
        self.assertEqual(["http://example.com"],
                         find_urls("link: http://example.com"))
        self.assertEqual(["https://yandex.ru"],
                         find_urls("link: https://yandex.ru"))
        self.assertEqual(["https://www.google.com"],
                         find_urls("link: https://www.google.com "))

    def test_find_urls_with_www_prefix(self):
        self.assertEqual(["www.example.com"],
                         find_urls("www.example.com is a link, example.org is not a link"))
        self.assertEqual(["https://www.wikipedia.org/wiki"],
                         find_urls("https://www.wikipedia.org/wiki"))
        self.assertEqual(["www.wikipedia.org/wiki"],
                         find_urls("www.wikipedia.org/wiki"))

    def test_find_urls_with_path(self):
        self.assertEqual(["https://www.wikipedia.org/wiki/Philosophy"],
                         find_urls("https://www.wikipedia.org/wiki/Philosophy"))
        self.assertEqual(["www.wikipedia.org/wiki/Philosophy"],
                         find_urls("www.wikipedia.org/wiki/Philosophy"))

    def test_not_find_urls(self):
        self.assertEqual([],
                         find_urls("https://ru.wikipedia.org"))
        self.assertEqual([],
                         find_urls("ru.wikipedia.org"))
        self.assertEqual([],
                         find_urls("This is just a regular text without any URLs."))
        self.assertEqual([],
                         find_urls("Some email addresses like user@example.com should not be considered as URLs."))
        self.assertEqual([],
                         find_urls("This is a phone number: +1234567890."))
        self.assertEqual([],
                         find_urls("Invalid URL: http://examp le.com/path with spaces"))
        self.assertEqual([],
                         find_urls("Invalid URL: ftp://example.com"))
        self.assertEqual([],
                         find_urls("Invalid URL: https://example.c-om"))
        self.assertEqual([],
                         find_urls("Invalid URL: ht+tp://example.com"))
        self.assertEqual([],
                         find_urls("Invalid URL: http:/-/example.com/path."))
        self.assertEqual(["http://example.com/path"],
                         find_urls("Invalid URL: http://example.com/path#/notvalid"))

    def test_find_urls_at_text(self):
        self.assertEqual(['https://www.coursera.org',
                          'https://www.edx',
                          'https://www.mit',
                          'https://www.stanford.edu',
                          'https://nips.cc',
                          'https://icml.cc'],
                         find_urls("""
В эпоху цифровизации искусственный интеллект и машинное обучение играют ключевую роль в различных сферах жизни. С каждым годом количество онлайн-курсов и ресурсов, посвященных этой теме, растет. Например, [Coursera](https://www.coursera.org/) и [edX](https://www.edx.org/) предлагают широкий спектр курсов по машинному обучению, начиная от вводных до продвинутых.

Однако, обучение не ограничивается онлайн-платформами. Многие университеты предлагают программы магистратуры и докторантуры по машинному обучению. Например, [Массачусетский технологический институт](https://www.mit.edu/) (MIT) и [Стэнфордский университет](https://www.stanford.edu/) активно развивают исследования в этой области и предлагают программы обучения.

Большинство исследований по машинному обучению публикуется в научных журналах и конференциях. Например, [NeurIPS](https://nips.cc/) и [ICML](https://icml.cc/) - это крупнейшие конференции, посвященные исследованиям в области искусственного интеллекта и машинного обучения.

С развитием технологий возрастает и интерес к применению машинного обучения в различных отраслях. Например, в медицине для диагностики заболеваний и разработки новых методов лечения, в финансовой сфере для прогнозирования рынка и минимизации рисков, в транспортной сфере для создания автономных транспортных средств и управления трафиком.

Несмотря на все преимущества, машинное обучение также внушает опасения. Вопросы приватности данных, потенциальных ошибок и предвзятости алгоритмов, а также недостаточной защиты от кибератак становятся все более актуальными.

Тем не менее, с правильным подходом машинное обучение может стать мощным инструментом для решения сложных задач и улучшения качества жизни людей.

                         """))


if __name__ == '__main__':
    unittest.main()
