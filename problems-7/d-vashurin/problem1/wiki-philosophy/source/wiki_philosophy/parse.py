__all__ = (
    "is_normal_link",
    "find_normal_link",
    "to_article",
)

from bs4 import Tag

from wiki_philosophy.consts import INTERNAL_SEGMENT, WIKIPEDIA_ROOT

BANNED_PREFIXES = (
    "#",
    "/wiki/Help:",
    "/wiki/File:",
    "/wiki/Wikipedia:",
    "/wiki/Template:",
)
BANNED_TEXTS = {
    "[citation needed]"
    "citation needed",
    "[note 1]",
    "[note 2]",
}


def is_normal_link(a: Tag) -> bool:
    if a.has_attr("class") and "image" in a.attrs["class"]:
        return False

    if any(a.attrs["href"].startswith(banned) for banned in BANNED_PREFIXES):
        return False

    if a.has_attr("role") and a.attrs["role"] == "button":
        return False

    if a.text.startswith("(") and a.text.endswith(")"):
        return False

    if a.text.strip() in BANNED_TEXTS:
        return False

    if (parent := a.parent) is None:
        return True

    if parent.name == "span" and parent.has_attr("class") and "reference" in parent.attrs["class"]:
        return False

    return True


def find_normal_link(parser: Tag, /) -> str | None:
    article_content = parser.find("div", id="mw-content-text")
    if article_content is None or not isinstance(article_content, Tag):
        return None

    for paragraph in article_content.find_all("p"):
        if not isinstance(paragraph, Tag):
            continue

        for a in paragraph.find_all("a", href=True):
            if isinstance(a, Tag) and is_normal_link(a):
                return a.attrs["href"]

    return None


def to_link(article: str) -> str:
    return f"{WIKIPEDIA_ROOT}/{INTERNAL_SEGMENT}/{article}"


def to_article(internal_link: str) -> str:
    return internal_link.removeprefix(f"/{INTERNAL_SEGMENT}/")
