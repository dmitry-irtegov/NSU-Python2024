import re


def find_urls(text):
    pattern = r"\b(?:https?://|www\.|https?://www\.)\w+\.\w{2,3}(?:/\w+|)*\b"
    urls = re.findall(pattern, text)
    return urls
