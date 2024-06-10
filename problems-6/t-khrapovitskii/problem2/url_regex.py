import re
import sys
from typing import Iterable, Any


def read_domains() -> Iterable[str]:
    try:
        with open('tlds-alpha-by-domain.txt', 'r') as f:
            return map(lambda x: x.strip().lower(),
                       filter(lambda line: not (line.startswith('#') or line.startswith("XN-")),
                              f.readlines()))
    except Exception as e:
        print("Error when reading `tlds-alpha-by-domain.txt` that should be in same directory as python file",
              file=sys.stderr)
        print(e, file=sys.stderr)
        exit(1)


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
# known_domains_iter = ['ru', 'com']
known_domains_iter = read_domains()
known_domains = r"(\.(" + '|'.join(known_domains_iter) + r")\b)"
# language=RegExp
path = r"(/[{0}]+(/[{0}]*)*)?/?".format(pchar)
by_scheme = known_schemes + authority + path
by_www = scheme + "?" + r"www\." + authority + path
by_domain = scheme + "?" + authority + known_domains + path
# noinspection RegExpDuplicateAlternationBranch
pattern = re.compile(f"\\b({by_scheme})|({by_www})|({by_domain})\\b", flags=re.IGNORECASE)

# print(by_scheme)
print(by_www)


# print(by_domain)
# print(pattern.pattern)

def find_urls(text: str) -> Iterable[tuple[Any, Any]]:
    return map(lambda i: (i.start(), i.end()), re.finditer(pattern, text))
