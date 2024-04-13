import argparse
import sys


sys.path.append(sys.argv[0]+"/../../.")
from affinecipher.core.ciphers import AffineCipher
from affinecipher.language import Language

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', type=Language, required=True)
    args = parser.parse_args()
    print(AffineCipher.keygen(args.language))
