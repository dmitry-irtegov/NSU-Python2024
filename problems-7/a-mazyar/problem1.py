import requests
from bs4 import BeautifulSoup
from time import sleep

WIKI_LINK_BASE = "https://en.wikipedia.org/wiki/"

def is_wiki_normal(wiki_link: str) -> bool:
    '''
    Checks if link is a blue link to some wiki page. Help: are omittable help links
    '''
    return 'href' in wiki_link.attrs and wiki_link['href'].find("/wiki/") != -1 and wiki_link['href'].find("Help:") == -1

def seek_philosopy(article: str) -> str:
    result = (article, )
    while article != "Philosophy":
        sleep(2)
        url = ''.join((WIKI_LINK_BASE, article))
        response = requests.get(
            url=url,
        )
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # the idea is to take first paragraph and look for the first link there
        normal_link_found = False
        for paragraph in soup.find(id="mw-content-text").find_all("p"):
            links = list(filter(is_wiki_normal, paragraph.find_all("a")))
            if len(links) != 0:
                article = links[0]['href'][6:]
                normal_link_found = True
                break

        if article in result:
            raise Exception("Philosophy wasn't reached: Loop occured")

        if not normal_link_found:
            raise Exception("Philosophy wasn't reached: No more links to follow")
        
        result += (article, )
        print(article)

    print(" -> ".join(result))
    return result

if __name__ == "__main__":
    seek_philosopy("Cell_division")