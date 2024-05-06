import argparse
import requests
import pickle
import time
from html.parser import HTMLParser

def wiki_searcher(start_link):
    wiki_index = start_link.find('/wiki/')
    if wiki_index == -1:
        raise ValueError("Your start link is not from Wiki")
    try:
        with open("cache.pkl", mode="rb") as file:
            cache = pickle.load(file)
    except FileNotFoundError:
        cache = {}
    links_cache = {}
    philLink = '/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'
    cnt = 0
    next_link = start_link[wiki_index:]
    
    while True:
        if next_link in cache.keys():
            content = cache[next_link]
        else:
            content = requests.get('https://ru.wikipedia.org' + next_link).text
            cache[next_link] = content
        parser = MyHTMLParser()
        try:
            parser.feed(content)
        except StopParsing as ex:
            current_link = next_link
            title, next_link = ex.args
            print(cnt, title)
            cnt = cnt + 1
            if next_link in links_cache.keys():
                print(links_cache[next_link])
                print("Цикл!")
                break
            if next_link == philLink:
                print("Философия!")
                break
            links_cache[current_link] = title
            time.sleep(2)
    with open("cache.pkl", mode="wb") as file:
        pickle.dump(cache, file)

class MyHTMLParser(HTMLParser):
    
    tag = ''
    link_flag = False
    title_flag = False
    table_flag = False
    title = ''
    next_link = ''
    
    def handle_starttag(self, tag, attrs):
        
        if tag == 'p':
            self.tag = 'p'
            self.link_flag = True
            
        if tag == 'table':
            self.table_flag = True
            
        if tag == 'h1':
            self.tag = 'h1'
            self.title_flag = True
        
        if self.link_flag and tag == 'a' and not self.table_flag:
            for atr, value in attrs:
                if value.find('#cite') != -1:
                    break
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
        if tag == 'table':
            self.table_flag = False
        self.tag = ''
        

    def handle_data(self, data):
        
        if self.tag == 'link':
            self.close()
        
        if self.tag == 'title':
            self.title = data
            
    def close(self):
        
        raise StopParsing(self.title, self.next_link)
    
class StopParsing(Exception):
    
    def __init__(self, title, next_link):
        super().__init__(title, next_link)
        self.strerror = "No errors, just wanna stop parsing"
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start_link", help="enter your start link here")
    args = parser.parse_args()
    try:
        wiki_searcher(args.start_link)
    except Exception as e:
        print(e)