# -*- coding: utf-8 -*-
import argparse
from tr import tr

parser = argparse.ArgumentParser()
parser.add_argument("replace_from", help="Строка символов для замены")
parser.add_argument("replace_to", help="Строка символов замены")
parser.add_argument("-d", "--delete", help="Список символов для удаления")
args = parser.parse_args()

string = input()
print(tr(string, args.replace_from, args.replace_to, args.delete))

