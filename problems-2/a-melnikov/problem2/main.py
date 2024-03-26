from io import TextIOWrapper
import sys

LangDict = dict[str, set[str]]


def _lat_eng_to_eng_lat(d: LangDict) -> LangDict:
    res: LangDict = dict()
    for key, val in d.items():
        for word in val:
            if word in res:
                res[word].add(key)
            else:
                res[word] = set([key])
    return res


def _parse_dict(file: TextIOWrapper) -> LangDict:
    res = dict()
    for s in file:
        word, meanings = s.strip().split(" - ")
        value = meanings.split(", ")
        res[word] = set(value)
    return res


def _write_dict(file: TextIOWrapper, d: LangDict):
    for key, val in sorted(d.items()):
        file.write("{} - {}\n".format(key, ", ".join(sorted(val))))


def convert(latengdictname: str, englatdictname: str):
    try:
        file = open(latengdictname, "r")
    except Exception as e:
        print(e, file=sys.stderr)
        return

    with file:
        res = _lat_eng_to_eng_lat(_parse_dict(file))

    try:
        file = open(englatdictname, "w")
    except Exception as e:
        print(e, file=sys.stderr)
        return

    with file:
        _write_dict(file, res)


if __name__ == "__main__":
    convert("resources/lat-eng_dict.txt", "resources/eng-lat_dict.txt")
