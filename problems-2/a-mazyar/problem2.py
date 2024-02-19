import unittest
import re

def parse_thes_entry(thesaurus, entry):
    words = re.split(r'[,-]', entry)
    words = list(map(lambda s: s.strip(), words))
    thesaurus[words[0]] = words[1:]

def read_file_thes(file_name):
    thesaurus = {}
    with open(file_name) as f:
        for line in f:
            parse_thes_entry(thesaurus, line)

    return thesaurus

def push_sorted(list, new_entry):
    if list:
        for i, entry in enumerate(list):
            if new_entry < entry:
                list.insert(i, new_entry)
                return
    
    list.append(new_entry)

def reverse_thes_pair(thesaurus, word, translation):
    if translation in thesaurus:
        push_sorted(thesaurus[translation], word)
    else:
        thesaurus[translation] = [word]

def reverse_thesaurus(thesaurus):
    rev_thes = {}
    for word, translations in thesaurus.items():
       for translation in translations:
           reverse_thes_pair(rev_thes, word, translation)
    return rev_thes

def format_thesaurus(thesaurus):
    str_thes = ""
    for word, trans in sorted(thesaurus.items()):
        str_thes += word
        str_thes += " - "
        str_thes += ", ".join(sorted(trans))
        str_thes += "\n"
    return str_thes

class TestThesaurusReverser(unittest.TestCase):  
    def test_same_translation(self):
        thes = {'apple': ["taku"], 'bird': ["taku"], 'train': ["taku"]}
        rev_thes = {"taku": ['apple', 'bird', 'train']}
        self.assertEqual(reverse_thesaurus(thes), rev_thes)

    def test_reverse_order(self):
        thes = {'train': ["taku"], 'bird': ["taku"], 'apple': ["taku"]}
        rev_thes = {"taku": ['apple', 'bird', 'train']}
        self.assertEqual(reverse_thesaurus(thes), rev_thes)

    def test_permutations(self):
        thes = {'apple': ['bird', 'train'], 'bird': ['apple', 'train'], 'train': ['apple', 'bird']}
        self.assertEqual(reverse_thesaurus(thes), thes)

if __name__ == "__main__":
    print(format_thesaurus(reverse_thesaurus(read_file_thes('thesaurus.txt'))))
    unittest.main()