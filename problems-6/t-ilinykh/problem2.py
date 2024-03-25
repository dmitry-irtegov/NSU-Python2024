import re
import unittest

def find_urls(example_data):
    if not isinstance(example_data, str):
        raise TypeError("example_data must be a string")
    pattern = r"(?:https?:\/\/|www\.)(?:(?![.,?!;:()]*(?:\s|$))[^\s]){2,}"
    urls = re.findall(pattern, example_data)
    return urls


class TestFindURLs(unittest.TestCase):

    def test_single_url(self):
        text = "Visit us at www.example.com"
        self.assertEqual(find_urls(text), ["www.example.com"])

    def test_multiple_urls(self):
        text = "Visit us at www.example.com or at www.test-example.org"
        self.assertEqual(find_urls(text), ["www.example.com", "www.test-example.org"])

    def test_url_with_dash_and_underscore(self):
        text = "Check out www.test-example.org and www.test_example.org"
        self.assertEqual(find_urls(text), ["www.test-example.org", "www.test_example.org"])

    def test_url_with_subdomains(self):
        text = "Visit www.sub.example.com and www.sub.sub.example.com"
        self.assertEqual(find_urls(text), ["www.sub.example.com", "www.sub.sub.example.com"])

    def test_url_with_different_tlds(self):
        text = "Visit www.example.net, www.example.org, and www.example.co.uk"
        self.assertEqual(find_urls(text), ["www.example.net", "www.example.org", "www.example.co.uk"])

    def test_url_with_invalid_characters(self):
        text = "www.example!.com"
        self.assertEqual(find_urls(text), ["www.example!.com"])

    def test_url_without_www_prefix(self):
        text = "Visit us at example.com"
        self.assertEqual(find_urls(text), [])

    def test_url_with_digits_in_tld(self):
        text = "Visit www.example123.com"
        self.assertEqual(find_urls(text), ["www.example123.com"])

    def test_url_with_single_letter_tld(self):
        text = "Visit www.example.a"
        self.assertEqual(find_urls(text), ["www.example.a"])

    def test_url_with_short_tld(self):
        text = "Visit www.example.co"
        self.assertEqual(find_urls(text), ["www.example.co"])

    def test_url_with_long_tld(self):
        text = "Visit www.example.travel"
        self.assertEqual(find_urls(text), ["www.example.travel"])

    def test_single_http_url(self):
        text = "Visit us at http://www.example.com"
        self.assertEqual(find_urls(text), ["http://www.example.com"])

    def test_multiple_http_urls(self):
        text = "Visit us at http://www.example.com or at http://www.test-example.org"
        self.assertEqual(find_urls(text), ["http://www.example.com", "http://www.test-example.org"])

    def test_http_url_with_dash_and_underscore(self):
        text = "Check out http://www.test-example.org and http://www.test_example.org"
        self.assertEqual(find_urls(text), ["http://www.test-example.org", "http://www.test_example.org"])

    def test_http_url_with_subdomains(self):
        text = "Visit http://www.sub.example.com and http://www.sub.sub.example.com"
        self.assertEqual(find_urls(text), ["http://www.sub.example.com", "http://www.sub.sub.example.com"])

    def test_http_url_with_digits_in_tld(self):
        text = "Visit http://www.example123.com"
        self.assertEqual(find_urls(text), ["http://www.example123.com"])

    def test_http_url_with_single_letter_tld(self):
        text = "Visit http://www.example.a"
        self.assertEqual(find_urls(text), ["http://www.example.a"])

    def test_http_url_with_short_tld(self):
        text = "Visit http://www.example.co"
        self.assertEqual(find_urls(text), ["http://www.example.co"])

    def test_http_url_with_long_tld(self):
        text = "Visit http://www.example.travel"
        self.assertEqual(find_urls(text), ["http://www.example.travel"])

    def test_invalid_example_data_type(self):
        with self.assertRaises(TypeError):
            find_urls(123)

if __name__ == '__main__':
    unittest.main()
