import re
import unittest


def find_urls(text):
    url_pattern = re.compile(r'\b(?:https?://|www\.)[\w.-]+\.\w{2,}(?:/\S*)?\b')
    return url_pattern.findall(text)


class TestFindUrls(unittest.TestCase):

    def test_https_url(self):
        text = "Secure site is https://secure-site.org and it is safe"
        expected = ['https://secure-site.org']
        self.assertEqual(find_urls(text), expected)

    def test_www_url(self):
        text = "Visit www.example.com for more information"
        expected = ['www.example.com']
        self.assertEqual(find_urls(text), expected)

    def test_multiple_urls(self):
        text = "Check these sites: http://example.com, https://site.org, and www.example.net."
        expected = ['http://example.com', 'https://site.org', 'www.example.net']
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_paths(self):
        text = "Go to http://example.com/path or https://site.org/anotherpath for details"
        expected = ['http://example.com/path', 'https://site.org/anotherpath']
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_subdomains(self):
        text = "Visit http://sub.example.com and https://secure.site.org"
        expected = ['http://sub.example.com', 'https://secure.site.org']
        self.assertEqual(find_urls(text), expected)

    def test_no_urls(self):
        text = "There are no URLs in this text."
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_trailing_punctuation(self):
        text = "Look at this: http://example.com, isn't it cool?"
        expected = ['http://example.com']
        self.assertEqual(find_urls(text), expected)

    def test_urls_in_parentheses(self):
        text = "Visit (http://example.com) for more details."
        expected = ['http://example.com']
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_numbers(self):
        text = "Our site is httpp://asd.com and a.dew.ewr and wwww.sd.ry and http://123site.com it's great!"
        expected = ['http://123site.com']
        self.assertEqual(find_urls(text), expected)


if __name__ == '__main__':
    unittest.main()
