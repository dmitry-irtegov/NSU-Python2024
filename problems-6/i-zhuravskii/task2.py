import re
import unittest


def find_urls(text):
    url_pattern = re.compile(r'\b(?:https?://|www\.)[\w.-]+\.\w{2,}(?:/\S*)?\b')
    return url_pattern.findall(text)


class TestFindUrls(unittest.TestCase):
    def test_basic_urls(self):
        text = "Visit www.example.com for more information."
        expected = ["www.example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_multiple_urls(self):
        text = "Check out www.example.com and www.test.org for more details."
        expected = ["www.example.com", "www.test.org"]
        self.assertEqual(find_urls(text), expected)

    def test_no_urls(self):
        text = "There are no URLs in this sentence."
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_subdomains(self):
        text = "Subdomains like www.blog.example.com should be found."
        expected = ["www.blog.example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_dashes(self):
        text = "Visit our site at www.example-site.com for updates."
        expected = ["www.example-site.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_different_tlds(self):
        text = "Sites like www.example.co.uk and www.example.org are common."
        expected = ["www.example.co.uk", "www.example.org"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_numbers(self):
        text = "Check out www.example123.com and www.456example.com."
        expected = ["www.example123.com", "www.456example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_at_text_boundaries(self):
        text = "www.start.com in the beginning and www.end.com at the end."
        expected = ["www.start.com", "www.end.com"]
        self.assertEqual(find_urls(text), expected)

    def test_text_with_punctuation(self):
        text = "Punctuation, such as www.example.com, should not affect the result."
        expected = ["www.example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_short_tlds(self):
        text = "Short TLDs like www.example.io and www.test.co should be found."
        expected = ["www.example.io", "www.test.co"]
        self.assertEqual(find_urls(text), expected)

    def test_text_with_non_url_like_www(self):
        text = "Words like www and wwwtest should not be treated as URLs."
        expected = []
        self.assertEqual(find_urls(text), expected)


if __name__ == '__main__':
    unittest.main()
