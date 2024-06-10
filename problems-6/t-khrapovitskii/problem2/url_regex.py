import re
from typing import Iterable, Any

# language=RegExp
# noinspection RegExpRedundantEscape
unreserved = r"a-z0-9\.\-_~"
# language=RegExp
pchar = unreserved + r":@"
# language=RegExp
scheme = r"(a-z[a-z0-9+\-.]://)"
known_schemes_iter = ['http', 'https']
known_schemes = f"(\\b({'|'.join(known_schemes_iter)})://)"
# language=RegExp
reg_name = r"[{0}]+(\.[{0}]+)*".format(unreserved.replace(r'\.', r''))
host = reg_name
authority = host
# language=RegExp
path = r"(/[{0}]+(/[{0}]*)*)?/?".format(pchar)
by_scheme = known_schemes + authority + path
by_www = scheme + "?" + r"www\." + authority + path
# noinspection RegExpDuplicateAlternationBranch
pattern = re.compile(f"\\b({by_scheme})|({by_www})\\b", flags=re.IGNORECASE)


# print(by_scheme)
# print(by_www)
# print(by_domain)
# print(pattern.pattern)

def find_urls(text: str) -> Iterable[tuple[Any, Any]]:
    return map(lambda i: (i.start(), i.end()), re.finditer(pattern, text))
