import argparse
import requests
import requests_cache
import time
import sys
from html.parser import HTMLParser

def wiki_searcher(start_link):
    wiki_index = start_link.find('/wiki/')
    if wiki_index == -1:
        raise ValueError("Your start link is not from Wiki")
    try:
        session = requests_cache.CachedSession('requests_cache')
    except BaseException as e:
        raise e("Error with cache file")
    links_cache = {}
    philLink = '/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F'
    random_link = '/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    cnt = 0
    next_link = start_link[wiki_index:]
    
    while True:
        if next_link.find('wikipedia.org') != -1:
            raise LinkIsNotFromRussianWiki("Current page contains a link to Wikipedia of another language")
        if next_link != random_link:
            content = session.get('https://ru.wikipedia.org' + next_link).text
        else:
            content = requests.get('https://ru.wikipedia.org' + next_link).text
        parser = MyHTMLParser()
        try:
            parser.feed(content)
        except StopParsing as ex:
            current_link = next_link
            title, next_link, multiple_link = ex.args
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
            if not(session.cache.contains(url = 'https://ru.wikipedia.org' + next_link)):
                time.sleep(1)
            if multiple_link:
                next_link = multiple_link_processing(next_link, session)
                
def multiple_link_processing(link, session):
    content = session.get('https://ru.wikipedia.org' + link).text
    parser = MultipleLinkParser()
    try:
        parser.feed(content)
    except StopParsing as ex:
        _, next_link, _ = ex.args
        return next_link
    raise MultipleLinkError("Error while processing multiple link: " + link)
    
class MyHTMLParser(HTMLParser):
    
    tag = ''
    link_flag = False
    title_flag = False
    table_flag = False
    no_bracket_flag = True
    
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
        
        if self.link_flag and tag == 'a' and not self.table_flag and self.no_bracket_flag:
            for atr, value in attrs:
                if value.find('#cite') != -1:
                    break
                if atr == 'href':
                    self.tag = 'link'
                    self.next_link = value
            for atr, value in attrs:
                if atr == 'class' and value == 'mw-disambig':
                    self.tag = 'multiple_link'
            
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
        
        if self.link_flag:
            if data.count('(') > data.count(')'):
                self.no_bracket_flag = False
            else:
                if data.count('(') < data.count(')'):
                    self.no_bracket_flag = True
        
        if self.tag == 'link':
            self.close(False)
            
        if self.tag == 'multiple_link':
            self.close(True)
        
        if self.tag == 'title':
            self.title = data
            
    def close(self, multiple_link_flag):
        raise StopParsing(self.title, self.next_link, multiple_link_flag)
    
class MultipleLinkParser(HTMLParser):
    
    previous_tag = ''
    next_link = ''
    
    def handle_starttag(self, tag, attrs):
        
        if tag == 'ul':
            self.previous_tag = 'ul'
            
        if tag == 'li' and self.previous_tag == 'ul':
            self.previous_tag = 'li'
            
        if tag == 'a' and self.previous_tag == 'li':
            for atr, value in attrs:
                if value.find('#cite') != -1:
                    break
                if atr == 'href':
                    self.previous_tag = 'link'
                    self.next_link = value

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.previous_tag == 'link':
            self.close()
            
    def close(self):
        raise StopParsing('', self.next_link, False)
    
class StopParsing(Exception):
    
    def __init__(self, title, next_link, multiple_link_flag):
        self.strerror = "No errors, just wanna stop parsing"
        super().__init__(title, next_link, multiple_link_flag)
        
class LinkIsNotFromRussianWiki(Exception):
    
    def __init__(self, message):
        super().__init__(message)
        
class MultipleLinkError(Exception):
    
    def __init__(self, message):
        super().__init__(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start_link", help="enter your start link here")
    args = parser.parse_args()
    try:
        wiki_searcher(args.start_link)
    except Exception as e:
        print(type(e).__name__, ': ', e, file=sys.stderr, sep = '')
    #wiki_searcher('https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B7%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5')