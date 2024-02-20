import requests
from bs4 import BeautifulSoup

def get_first_normal_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content_div = soup.find('div', id='mw-content-text')
    if content_div is None:
        return None
    paragraphs = content_div.find_all('p')
    for paragraph in paragraphs:
        links = paragraph.find_all('a', href=True)
        for link in links:
            if is_normal_link(link):
                return link['href']
    return None

def is_normal_link(link):
    # Exclude links with specific classes or styles
    if link.has_attr('class') and 'image' in link['class']:
        return False
    if link.parent.name == 'span' and link.parent.has_attr('class') and 'reference' in link.parent['class']:
        return False
    # Exclude links with specific text
    excluded_texts = ['[citation needed]', 'citation needed', '[note 1]', '[note 2]']
    if link.text.strip() in excluded_texts:
        return False
    # Exclude links in parentheses
    if '(' in link.text and ')' in link.text:
        return False
    return True

def follow_philosophy_law(start_url):
    flag = 1
    visited_urls = set()
    url = start_url
    while url not in visited_urls:
        visited_urls.add(url)
        print(url)
        next_url = get_first_normal_link('https://en.wikipedia.org' + url)
        if next_url is None:
            print("No normal links found.")
            break
        if next_url == '/wiki/Philosophy':
            print(next_url)
            print("Reached Philosophy. Stopping.")
            flag = 0
            break
        url = next_url
    if flag:
        print(url)
        print("Cycle detected.")

# Пример использования
start_url = '/wiki/Netflix'
follow_philosophy_law(start_url)
start_url = '/wiki/Python_(programming_language)'
follow_philosophy_law(start_url)
