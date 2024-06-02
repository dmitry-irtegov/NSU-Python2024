import argparse
import sys

from cipher.core.entity.language import Language
from cipher.table.cipher import TableCipher
sys.path.append(sys.argv[0] + "/../../.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', type=str, required=True)
    args = parser.parse_args()
    try:
        print(TableCipher.keygen(Language(args.language)))
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)
