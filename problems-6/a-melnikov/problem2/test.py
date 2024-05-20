import unittest
from main import find_urls

class TestUrlFinder(unittest.TestCase):
    
    def test_single_http_url(self) -> None:
        text = "Check out this website: https://example.com"
        self.assertEqual(find_urls(text), ['https://example.com'])

    def test_multiple_urls(self) -> None:
        text = "Visit www.google.com or https://stackoverflow.com for more information."
        self.assertEqual(find_urls(text), ['www.google.com', 'https://stackoverflow.com'])

    def test_no_urls(self) -> None:
        text = "This text does not contain any URLs."
        self.assertEqual(find_urls(text), [])

    def test_mixed_urls(self) -> None:
        text = "Check out these URLs: www.example.com and https://example.org"
        self.assertEqual(find_urls(text), ['www.example.com', 'https://example.org'])

    def test_invalid_urls(self) -> None:
        text = "Invalid URL: http://www..com"
        self.assertEqual(find_urls(text), [])

if __name__ == "__main__":
    unittest.main()
