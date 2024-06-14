from sys import stdin


def convert_complex(s: str) -> complex:
    s = s.strip().replace(' ', '').replace('i', 'j').replace('I', 'j').replace(',', '.')
    return complex(s)


def is_complex(s: str) -> bool:
    try:
        convert_complex(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    for line in stdin:
        try:
            converted = convert_complex(line)
            print('Got complex number:', converted)
            break
        except ValueError:
            print('Not a number')
