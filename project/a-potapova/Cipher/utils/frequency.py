import argparse
import json
import sys

import cipher.table.entity.frequencydata as frequency
from cipher.table.entity.text import TableText

sys.path.append(sys.argv[0]+"/../../.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=argparse.FileType('r', encoding="utf-8"), default=sys.stdin, help="Input file")
    parser.add_argument("--output", type=argparse.FileType('w', encoding="utf-8"), default=sys.stdout, help="Output file")
    args = parser.parse_args()
    try:
        text = ""
        for line in args.input:
            text += line
        freq = frequency.text_to_frequencies(TableText(text))
        json.dump(freq, args.output, indent=4)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)
