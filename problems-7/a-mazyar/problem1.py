import requests
import regex
from bs4 import BeautifulSoup
from time import sleep

WIKI_LINK_BASE = "https://en.wikipedia.org/wiki/"

def is_wiki_normal(wiki_link: str) -> bool:
    '''
    Checks if link is a blue link to some wiki page and isn't a note
    '''
    if 'role' in wiki_link.attrs and wiki_link['role'] == "note":
        return False
    
    return 'href' in wiki_link.attrs and wiki_link['href'].find("/wiki/") != -1

def remove_parentheses(text: str) -> str:
    return regex.sub("\(([^()]|(?R))*\)", "", text)

def seek_philosopy(article: str) -> str:
    result = (article, )
    while article != "Philosophy":
        sleep(2)
        url = ''.join((WIKI_LINK_BASE, article))
        try:
            response = requests.get(
                url=url,
            )
        except requests.exceptions.RequestException as e:
            print("Trouble connecting to the wiki page. Shutting down\n")
            raise SystemExit(e)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        link_found: bool = False
        for paragraph in soup.find(id="mw-content-text").find_all("p"):
            # we create artificial paragraph where all parantheses and their contents were removed
            psoup = BeautifulSoup()
            p = psoup.new_tag('p')
            p.append(BeautifulSoup(remove_parentheses(str(paragraph)), 'html.parser'))
            psoup.append(p)

            links = list(filter(is_wiki_normal, psoup.find_all("a")))
            if len(links) != 0:
                article = links[0]['href'][6:] # remove 'wiki/' part
                link_found = True
                break

        if not link_found:
            raise Exception("Philosophy wasn't reached: No more links to follow")
        
        if article in result:
            raise Exception("Philosophy wasn't reached: Loop occured")
        
        result += (article, )
        print(article)

    print(" -> ".join(result))
    return result

if __name__ == "__main__":
    seek_philosopy("Tzimmes")