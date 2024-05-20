import sys


def make_dictionary(path):
    try:
        with open(path, 'r') as input_file:
            result = dict()
            for line in input_file.readlines():
                line = line.strip()
                word, translations = line.split(' - ')
                for translation in translations.split(', '):
                    if translation in result.keys():
                        result[translation].append(word)
                    else:
                        result[translation] = [word]
    except Exception as e:
        e.additional_info = "Error with reading file"
        raise e
    try:
        with open(f'{path.replace(".txt", "")}_output.txt', 'w') as output_file:
            output_file.write('\n'.join(f'{word} - {", ".join(sorted(result[word]))}' for word in sorted(result)))
    except Exception as e:
        e.additional_info = "Error with writing file"
        raise e


if __name__ == '__main__':
    file_name = input("Enter file name: ")
    try:
        make_dictionary(file_name)
    except Exception as err:
        sys.stderr.write(f'{err.additional_info}: {repr(err)}')
        exit(1)
