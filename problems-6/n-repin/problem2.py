import re
import unittest

url_regex = re.compile(r'\b(?:http?://|www\.|http?://www\.)\w+\.\w{2,}(?:/\w+|)*\b')

def find_urls(text: str) -> list[str]:
    return url_regex.findall(text)

class FindUrlsTest(unittest.TestCase):
    def test_www_links(self):
        self.assertEqual(find_urls('Check out www.mydomain.com, it is nice'),
                         ['www.mydomain.com'])
        
        self.assertEqual(find_urls('Check out www.ya.com, it is nice, also check www.a.de'),
                         ['www.ya.com', 'www.a.de'])
        
        self.assertEqual(find_urls('Check out ww.ya.com, it is nice, also check .a.de and w3w.ya.ru'),
                         [])

    def test_http_links(self):
        self.assertEqual(find_urls('Check out http://mydomain.com, it is nice'),
                         ['http://mydomain.com'])
        
        self.assertEqual(find_urls('Check out http://mydomain.com, it is nice, also check http://hehe.com'),
                         ['http://mydomain.com', 'http://hehe.com'])
        
        self.assertEqual(find_urls('Check out htps://ya.com, it is nice, also check .a.de and http//.ya.ru or http:ya.ru'),
                         [])

    def test_tld(self):
        self.assertEqual(find_urls('Different valid TLD: www.my.com, www.my.de, www.my.travel, www.my.ru'),
                         ['www.my.com', 'www.my.de', 'www.my.travel', 'www.my.ru'])

    def test_path(self):
        self.assertEqual(find_urls('Links with paths: http://ya.ru/some/path and www.my.com/he/he/a/b/c'),
                         ['http://ya.ru/some/path', 'www.my.com/he/he/a/b/c'])
        
    def test_malformed(self):
        self.assertEqual(find_urls('Malformed links: http:/./ya.ru/some/path and http://...b.ru, http://a..c.com'),
                         [])
        
        self.assertEqual(find_urls('Malformed links: www./ya.ru/some/path and www/...b.ru, www/a..c.com'),
                         [])
        
        self.assertEqual(find_urls('Malformed links: hehe@mai.ru'),
                         [])

if __name__ == '__main__':
    unittest.main()