import re
from collections.abc import Generator

pattern = re.compile(r'(?P<hex>\\(x[0-7a-fA-F]{2}|u[0-7a-fA-F]{4}))|'
                     r'(?P<octal>\\[0-7]{1,3})|(?P<escape>\\.)|(?P<range>.-.)|(.|\n)',
                     flags=re.MULTILINE)


def parse_str(s: str) -> Generator[str, None, None]:
    seq = pattern.finditer(s)
    for match in seq:
        if match.group('hex'):
            yield chr(int(match.group('hex')[2:], 16))
        elif match.group('octal'):
            yield chr(int(match.group('octal')[1:], 8))
        elif match.group('escape'):
            match match.group('escape'):
                case '\\\\':
                    yield '\\'
                case '\\a':
                    yield '\a'
                case '\\b':
                    yield '\b'
                case '\\f':
                    yield '\f'
                case '\\n':
                    yield '\n'
                case '\\r':
                    yield '\r'
                case '\\t':
                    yield '\t'
                case '\\v':
                    yield '\v'
                case _:
                    raise ValueError(f'unknown escape sequence: {match.group('escape')}')
        elif match.group('range'):
            first = ord(match.group('range')[0])
            second = ord(match.group('range')[2])
            if first > second:
                first, second = second, first
            for i in range(first, second + 1):
                yield chr(i)
        else:
            yield match[0]


def make_replacement_map(string1: str, string2: str, delete: str | None = None, trunc=False) -> dict[str, str]:
    replacements = _make_replacement_map(string1, string2, trunc=trunc)
    if delete:
        for i in parse_str(delete):
            replacements[i] = ''
    return replacements


def _make_replacement_map(string1: str, string2: str, trunc=False) -> dict[str, str]:
    replacement: dict[str, str] = {}
    chars1 = parse_str(string1)
    chars2 = parse_str(string2)
    c1: str | None = None
    c2: str | None = None
    for c1 in chars1:
        try:
            c2 = next(chars2)
        except StopIteration:
            break
        replacement[c1] = c2
    if c1 is None or c2 is None or trunc:
        return replacement
    replacement[c1] = c2
    for c1 in chars1:
        replacement[c1] = c2
    return replacement


def replace(s: str, replacement_map: dict[str, str]) -> str:
    return ''.join(
        map(lambda x: replacement_map.get(x, x), s)
    )
