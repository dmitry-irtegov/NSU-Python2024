import requests
import time
import argparse

def wiki_searcher(start_link):
    infobox = '<table class="infobox'
    philLink = '%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F"'
    content = requests.get(startLink).text
    cnt = 0
    title_list = []
    new_link_flag = True

    while True:
        if new_link_flag:
            header_index = content.find('<span class="mw-page-title-main">') + 33
            header_index_end = content[header_index:].find('<') + header_index
            header = content[header_index:header_index_end]
            print(str(cnt) + ') ' + header)
        
            if header in title_list:
                print("Цикл!")
                break
            
            title_list.append(header)
            
        box_index = content.find(infobox) 
        if box_index != -1:
            box_index_end = content[box_index:].find('</table>')
            content = content[box_index_end:]
        
        start = content.find("<p>")
        end = content.find("</p>") + 1
        scope = content[start:end]
        content = content[end:]
        
        index = scope.find('<a href="/wiki/')
        if index == -1:
            new_link_flag = False
            print("Нет ссылки в абзаце")
            continue
        if scope[index:].find(philLink) != -1:
            cnt += 1
            print(str(cnt) + ') ' + "Философия")
            break
        index = index + 15
        
        index_end = scope[index:].find('"') + index
        
        link = scope[index : index_end]
        cnt += 1
        time.sleep(2)
        new_link_flag = True
        content = requests.get('https://ru.wikipedia.org/wiki/' + link).text
        
#startLink = 'https://ru.wikipedia.org/wiki/%D0%92%D1%81%D0%B5%D0%BC%D0%B8%D1%80%D0%BD%D0%B0%D1%8F_%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F'
#startLink = 'https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D1%84%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D0%B8'
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("start_link", help="enter your start link here")
    args = parser.parse_args()
    wiki_searcher(args.start_link) 