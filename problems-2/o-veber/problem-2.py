if __name__ == '__main__':
    filename = 'veber-dictionary.txt'
    with (open(filename) as file):
        my_dictionary = dict()
        for line in file.readlines():
            word, translations = line.split('-')
            word = word.strip()
            for translation in translations.split(','):
                translation = translation.strip()
                if translation not in my_dictionary:
                    my_dictionary[translation] = set()
                my_dictionary[translation].add(word)
    for key in my_dictionary:
        my_dictionary[key] = sorted(my_dictionary[key])
    print(my_dictionary)
