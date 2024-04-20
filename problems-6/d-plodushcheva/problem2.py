import unittest
import re


def find_url(string):
    if not isinstance(string, str):
        raise TypeError("String is needed")
    regex = r"(?:https?:\/\/|www\.)(?:(?![.,?!;:()]*(?:\s|$))[^\s]){2,}"
    urls = re.findall(regex, string)
    return urls


class TestFindURL(unittest.TestCase):
    def test_no_urls(self):
        text = "This is a text without any URLs."
        self.assertEqual(find_url(text), [])

    def test_single_http_url(self):
        text = "Check out this link: http://example.com"
        self.assertEqual(find_url(text), ["http://example.com"])

    def test_single_https_url(self):
        text = "Check out this link: https://example.com"
        self.assertEqual(find_url(text), ["https://example.com"])

    def test_single_www_url(self):
        text = "Visit our website at www.example.com"
        self.assertEqual(find_url(text), ["www.example.com"])

    def test_single_www_url_with_dash(self):
        text = "Visit our website at www.example-url.com"
        self.assertEqual(find_url(text), ["www.example-url.com"])

    def test_single_http_url_with_dash(self):
        text = "Visit our website at http://example-url.com"
        self.assertEqual(find_url(text), ["http://example-url.com"])

    def test_single_www_url_with_underscore(self):
        text = "Visit our website at www.example_url.com"
        self.assertEqual(find_url(text), ["www.example_url.com"])

    def test_single_http_url_with_underscore(self):
        text = "Visit our website at http://example_url.com"
        self.assertEqual(find_url(text), ["http://example_url.com"])

    def test_multiple_urls(self):
        text = "Here are some links: http://example.com and www.example.com"
        self.assertEqual(find_url(text), ["http://example.com", "www.example.com"])

    def test_url_with_subdomains(self):
        text = "Visit www.sub.example.com"
        self.assertEqual(find_url(text), ["www.sub.example.com"])

    def test_single_www_url_with_not_com(self):
        text = "Visit our website at www.example_url.ru"
        self.assertEqual(find_url(text), ["www.example_url.ru"])

    def test_url_without_www_prefix(self):
        text = "Visit us at example.com"
        self.assertEqual(find_url(text), [])

    def test_multiple_urls_with_digits(self):
        text = "Here are some links: http://example1.com, http://example2.com, www.example3.com"
        self.assertEqual(find_url(text), ["http://example1.com", "http://example2.com", "www.example3.com"])

    def test_invalid_http_url(self):
        text = "Visit us at hffp://example1.com"
        self.assertEqual(find_url(text), [])

    def test_invalid_www_url(self):
        text = "Visit us at wmw.example3.com"
        self.assertEqual(find_url(text), [])

    def test_invalid_www_url2(self):
        text = "Visit us at wmw.example3.co-m"
        self.assertEqual(find_url(text), [])

    def test_urls_with_ipv4_address(self):
        text = "Visit http://192.168.1.1"
        self.assertEqual(find_url(text), ["http://192.168.1.1"])

    def test_urls_with_fragment_identifier(self):
        text = "Navigate to https://example.com/page#section"
        self.assertEqual(find_url(text), ["https://example.com/page#section"])

    def test_urls_with_special_characters(self):
        text = ("Check out these URLs: http://example.com/page?query=string&param=value, "
                "https://example.com/path/to/page#section, www.example.com/index.html")
        self.assertEqual(find_url(text), ["http://example.com/page?query=string&param=value",
                                          "https://example.com/path/to/page#section", "www.example.com/index.html"])

    def test_urls_with_unicode_characters(self):
        text = "Visit us at https://résumé.com, http://cafés.net, and www.müller.de"
        self.assertEqual(find_url(text), ["https://résumé.com", "http://cafés.net", "www.müller.de"])

    def test_invalid_example_data_type(self):
        with self.assertRaises(TypeError):
            find_url(0)


if __name__ == '__main__':
    unittest.main()
