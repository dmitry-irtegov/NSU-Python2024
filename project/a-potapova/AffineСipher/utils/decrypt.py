import argparse
import sys

from affinecipher.language import define_language

sys.path.append(sys.argv[0]+"/../../.")
from affinecipher.core.ciphers import AffineCipher

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, required=True)
    parser.add_argument('--key', type=str, required=True)
    args = parser.parse_args()
    print(AffineCipher(define_language(args.text)).decrypt(args.text, key=args.key))
