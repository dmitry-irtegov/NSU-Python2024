import argparse
import sys


def init_parser():
    parser = argparse.ArgumentParser(description='Make alternative dictionary.')
    parser.add_argument('--input', type=str,
                        default='english-latin-dictionary.txt',
                        help='path to input file')
    parser.add_argument('--output', type=str,
                        default='latin-english-dictionary.txt',
                        help='path to output file')
    return parser


def parse_line(line: str):
    english_word, latin_words = line.split(" - ")
    latin_words = latin_words.split(", ")
    return english_word, latin_words


def reverse_dictionary(input_filename: str):
    result_dictionary = {}
    with open(input_filename, 'r') as file:
        for line in file:
            english_word, latin_words = parse_line(line.strip("\n"))
            for latin_word in latin_words:
                if latin_word in result_dictionary:
                    result_dictionary[latin_word].append(english_word)
                else:
                    result_dictionary[latin_word] = [english_word]
    return result_dictionary


def save_dictionary(dictionary: dict, output_filename: str):
    with open(output_filename, 'w') as file:
        for key in sorted(dictionary.keys()):
            file.write(key + " - ")
            for i, word in enumerate(sorted(dictionary[key])):
                if i != 0:
                    file.write(", ")
                file.write(word)
            file.write("\n")


if __name__ == '__main__':
    args = init_parser().parse_args()
    input_file = args.input
    output_file = args.output
    latin_dictionary = None
    try:
        latin_dictionary = reverse_dictionary(input_file)
    except Exception as e:
        sys.stderr.write(f"Error while reversing dictionary from file \"{input_file}\": {str(e)}")
        exit(1)
    try:
        save_dictionary(latin_dictionary, output_file)
    except Exception as e:
        sys.stderr.write(f"Error while saving dictionary to file \"{output_file}\": {str(e)}")
        exit(1)
