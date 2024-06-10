import unittest
import re

def find_url(line, urls):
    
    for match in re.finditer(r'((http(s)?://)?www\.|http(s)?://)(([a-zA-Z0-9]+(\-)*)+\.)+([a-zA-Z0-9]+(\-)*)*', line):
        end = line[match.end():].find(' ')
        if end == -1:
            path = line[match.end():]
        else:
            path = line[match.end():match.end()+end]
        urls.append(match[0] + path)
    return urls
        

def url_finder(filename):
    urls =[]
    file = open(filename, 'r')
    for line in file:
        find_url(line, urls)
    file.close()
    return urls

class TestUrls(unittest.TestCase):
  
    def test_simple(self):
        self.assertEqual(url_finder("input1.txt"), ['http://www.omim.org/entry/227220', 'https://www.kinopoisk1.ru/', 'https://www.kinopoisk2.ru/'])
    
    def test_atTheEndOfLine(self):
        self.assertEqual(url_finder("input2.txt"), ['www.om-im.org/entry/227220'])
        
    def test_noLink(self):
        self.assertEqual(url_finder("input3.txt"), [])
        
    def test_strangeLink(self):
        self.assertEqual(url_finder("input4.txt"), ['https://mysite.ru'])
        
    
if __name__ == "__main__":
  unittest.main()