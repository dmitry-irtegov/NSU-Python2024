
def anglo_latin_rearrange_sort(filename = "problems-2/n-batenko/english_latin_dictionary.txt"):
    dictionary = {}
    with open(filename) as f:

        for line in f:
            temp = line.split(" - ")
            eng = temp[0]
            latins = temp[1].split(", ")

            for word in latins:
                dictionary[word.strip()] = eng

    sorted_dict = {}
    sorted_keys = sorted(dictionary.keys())
    for k in sorted_keys:
        sorted_dict[k] = dictionary[k]
    
    return sorted_dict

def dict_printer(dictionary : dict):
    for k, v in dictionary.items():
        print(k, " - ", v)


dict_printer(anglo_latin_rearrange_sort())