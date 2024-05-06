import sys


def split_string(string):
    string = string.strip()
    english_word, latin_words = string.split(' - ')
    latin_words = latin_words.split(', ')
    return english_word, latin_words


def read_words(input_file_name):
    temp_dictionary = {}
    with open(input_file_name, 'r') as file:
        for line in file.readlines():
            english_word, latin_words = split_string(line)
            for latin_word in latin_words:
                if latin_word in temp_dictionary.keys():
                    temp_dictionary[latin_word].append(english_word)
                else:
                    temp_dictionary[latin_word] = [english_word]
    return temp_dictionary


def write_words(output_file_name, local_dictionary):
    with open(output_file_name, 'w') as file:
        for k, v in sorted(local_dictionary.items()):
            file.write(k + ' - ' + ', '.join(v) + '\n')


if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    try:
        dictionary = read_words(input_file)
    except Exception as e:
        sys.stderr.write(f"Error while reading file: \"{input_file}\": {str(e)}")
        exit(1)
    try:
        write_words(output_file, dictionary)
    except Exception as e:
        sys.stderr.write(f"Error while writing file: \"{output_file}\": {str(e)}")
        exit(1)
