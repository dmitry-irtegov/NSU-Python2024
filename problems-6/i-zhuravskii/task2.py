import re
import unittest


def find_urls(text):
    # Регулярное выражение для URL-адресов с обработкой портов и без некорректных URL
    url_pattern = re.compile(r'\b(?:https?://|www\.)[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?::\d+)?(?:/\S*)?\b')
    return [url for url in url_pattern.findall(text) if not re.search(r'https?://-', url)]


class TestFindUrls(unittest.TestCase):
    def test_basic_urls(self):
        text = "Visit www.example.com and http://example.com for more information."
        expected = ["www.example.com", "http://example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_multiple_urls(self):
        text = "Check out www.example.com, http://example.com, and https://example.org for more details."
        expected = ["www.example.com", "http://example.com", "https://example.org"]
        self.assertEqual(find_urls(text), expected)

    def test_no_urls(self):
        text = "There are no URLs in this sentence."
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_subdomains(self):
        text = "Visit www.blog.example.com, http://blog.example.com, and https://shop.example.com for info."
        expected = ["www.blog.example.com", "http://blog.example.com", "https://shop.example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_dashes(self):
        text = "Visit www.example-site.com and http://example-site.com for updates."
        expected = ["www.example-site.com", "http://example-site.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_different_tlds(self):
        text = "Sites like www.example.co.uk and https://example.org are common."
        expected = ["www.example.co.uk", "https://example.org"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_numbers(self):
        text = "Check out www.example123.com and http://456example.com."
        expected = ["www.example123.com", "http://456example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_paths(self):
        text = "Visit http://example.com/path, https://example.com/another/path, and www.example.com/path."
        expected = ["http://example.com/path", "https://example.com/another/path", "www.example.com/path"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_ports(self):
        text = "Check http://example.com:8080 and https://example.com:443 for port-specific sites."
        expected = ["http://example.com:8080", "https://example.com:443"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_query_parameters(self):
        text = "Go to http://example.com/?query=test and https://example.com/?search=value for searches."
        expected = ["http://example.com/?query=test", "https://example.com/?search=value"]
        self.assertEqual(find_urls(text), expected)

    def test_text_with_punctuation(self):
        text = "Punctuation, such as www.example.com, should not affect the result."
        expected = ["www.example.com"]
        self.assertEqual(find_urls(text), expected)

    def test_urls_with_short_tlds(self):
        text = "Short TLDs like www.example.io and https://example.co should be found."
        expected = ["www.example.io", "https://example.co"]
        self.assertEqual(find_urls(text), expected)

    def test_text_with_non_url_like_www(self):
        text = "Words like www and wwwtest should not be treated as URLs."
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_incorrect_urls(self):
        text = "Some incorrect URLs: http://example, www.example, http://.com, and https://-example.com."
        expected = []
        self.assertEqual(find_urls(text), expected)


if __name__ == '__main__':
    unittest.main()
