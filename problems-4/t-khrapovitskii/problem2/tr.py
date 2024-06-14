#!/usr/bin/env python3
import argparse
import sys
from util import replace, make_replacement_map


def main():
    try:
        parser = argparse.ArgumentParser(
            prog='tr.py',
            description='Changes one characters to another')
        parser.add_argument('STRING1')
        parser.add_argument('STRING2')
        parser.add_argument('-d', '--delete', type=str, help='delete characters in array DELETE, also translate')
        parser.add_argument('-t', '--truncate-set1', action='store_true', help='truncate ARRAY1 to length of ARRAY2')

        args = parser.parse_args()
        if not args.STRING1 or not args.STRING2:
            print("STRING1 and STRING2 must be not empty", file=sys.stderr)
            sys.exit(1)

        m = make_replacement_map(args.STRING1, args.STRING2, args.delete, args.truncate_set1)
        while True:
            s = input()
            print(replace(s, m))
    except (KeyboardInterrupt, EOFError):
        exit(0)


if __name__ == '__main__':
    main()
