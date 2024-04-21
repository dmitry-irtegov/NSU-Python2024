import argparse
import requests
import time
from html.parser import HTMLParser

def wiki_searcher(start_link):
    philLink = '/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'
    content = requests.get(start_link).text
    cnt = 0
    title_list = []
    work_flag = True
    
    while work_flag:
        parser = MyHTMLParser()
        try:
            parser.feed(content)
        except StopIteration as ex:
            title, next_link = ex.args
            print(cnt, title)
            cnt = cnt + 1
            if title in title_list:
                print("Цикл!")
                work_flag = False
            title_list.append(title)
            if next_link == philLink:
                print("Философия!")
                work_flag = False
            time.sleep(2)
            content = requests.get('https://ru.wikipedia.org' + next_link).text

class MyHTMLParser(HTMLParser):
    
    tag = ''
    link_flag = False
    title_flag = False
    title = ''
    next_link = ''
    
    def handle_starttag(self, tag, attrs):
        
        if tag == 'p':
            self.tag = 'p'
            self.link_flag = True
            
        if tag == 'h1':
            self.tag = 'h1'
            self.title_flag = True
        
        if self.link_flag and tag == 'a':
            for atr, value in attrs:
                if atr == 'href':
                    self.tag = 'link'
                    self.next_link = value
            
        if self.title_flag and tag == 'span':
            self.tag = 'title'

    def handle_endtag(self, tag):
        
        if tag == 'p':
            self.link_flag = False
        if tag == 'h1':
            self.title_flag = False
        self.tag = ''
        

    def handle_data(self, data):
        
        if self.tag == 'link':
            self.close()
        
        if self.tag == 'title':
            self.title = data
            
    def close(self):
        
        raise StopIteration(self.title, self.next_link)

# 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB-%D0%B4%D0%B5%D0%BC%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D1%8F_%D0%A2%D0%B8%D0%B1%D0%B5%D1%82%D0%B0'
# 'https://ru.wikipedia.org/wiki/%D0%92%D1%81%D0%B5%D0%BC%D0%B8%D1%80%D0%BD%D0%B0%D1%8F_%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F'
# 'https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D1%84%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D0%B8'
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start_link", help="enter your start link here")
    args = parser.parse_args()
    wiki_searcher(args.start_link)