import requests
import regex
from bs4 import BeautifulSoup
from time import sleep
from sys import stderr, exit

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
    print(article)
    while article != "Philosophy":
        sleep(2)
        url = ''.join((WIKI_LINK_BASE, article))
        try:
            response = requests.get(
                url=url,
            )
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print(f"Timeout while connecting to {url}. Shutting down", file=stderr)
            exit(-1)
        except requests.exceptions.ConnectionError as e:
            print(f"Troubles connecting to {url}. Shutting down\n\nError description:\n{e.args[0]}", file=stderr)
            exit(-1)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error occured when sending request to {url}. Shutting down.\n\nError description:\n{errh.args[0]}", file=stderr)
            exit(-1)
        except requests.RequestException:
            print(f"Troubles sending request to {url}. Shutting down")
            exit(-1)
        
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
            # index.php?title=MOS:FIRST&redirect=no
            print(f"Philosophy wasn't reached: No more links to follow from {url}", file=stderr)
            exit(-1)
        
        if article in result:
            # Tax
            print(f"Philosophy wasn't reached: Loop occured with {article} article", file=stderr)
            exit(-1)
        
        result += (article, )
        print(article)

    print(" -> ".join(result))
    return result

if __name__ == "__main__":
    seek_philosopy("Tzimmes")