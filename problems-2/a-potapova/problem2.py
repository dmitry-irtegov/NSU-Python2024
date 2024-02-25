def parse_line(line: str):
    english_word, latin_words = line.split(" - ")
    latin_words = latin_words.split(", ")
    return english_word, latin_words


def reverse_dictionary(input_filename: str, output_filename: str):
    dictionary = {}
    with open(input_filename, 'r') as file:
        line = file.readline().strip("\n")
        while line:
            english_word, latin_words = parse_line(line)

            for latin_word in latin_words:
                if latin_word in dictionary:
                    dictionary[latin_word].append(english_word)
                else:
                    dictionary[latin_word] = [english_word]

            line = file.readline().strip("\n")

    with open(output_filename, 'w') as file:
        keys = list(dictionary.keys())
        keys.sort()
        for key in keys:
            file.write(key + " - ")
            words = dictionary[key]
            words.sort()
            for i, word in enumerate(words):
                if i != 0:
                    file.write(", ")
                file.write(word)
            file.write("\n")


if __name__ == '__main__':
    reverse_dictionary('english-latin-dictionary.txt', 'latin-english-dictionary.txt')
