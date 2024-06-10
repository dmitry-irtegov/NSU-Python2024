import argparse
import sys

from cipher.table.cipher import TableCipher
from cipher.table.entity.key import TableKey
from cipher.table.entity.text import TableText

sys.path.append(sys.argv[0]+"/../../.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, required=True)
    parser.add_argument('--key', type=str, required=True)
    args = parser.parse_args()
    try:
        print(TableCipher.decrypt(TableText(args.text), key=TableKey(args.key)))
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)
