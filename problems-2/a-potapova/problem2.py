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
    keys = list(result_dictionary.keys())
    for key in keys:
        result_dictionary[key].sort()
    return result_dictionary


def save_dictionary(dictionary: dict, output_filename: str):
    with open(output_filename, 'w') as file:
        keys = list(dictionary.keys())
        keys.sort()
        for key in keys:
            file.write(key + " - ")
            for i, word in enumerate(dictionary[key]):
                if i != 0:
                    file.write(", ")
                file.write(word)
            file.write("\n")


if __name__ == '__main__':
    latin_dictionary = reverse_dictionary('english-latin-dictionary.txt')
    save_dictionary(latin_dictionary,  'latin-english-dictionary.txt')
