import unittest
import re
from timeit import Timer
from bisect import bisect_left
from random import randrange

def parse_thes_entry(thesaurus, entry):
    words = re.split(r'[,-]', entry)
    words = tuple(map(lambda s: s.strip(), words))
    thesaurus[words[0]] = words[1:]

def read_file_thes(file_name):
    thesaurus = {}
    with open(file_name) as f:
        for line in f:
            parse_thes_entry(thesaurus, line)

    return thesaurus

def push_sorted_old():
    arr = []
    for _ in range(10000):
        new_entry = randrange(0,100000)
        for i, entry in enumerate(arr):
            if new_entry < entry:
                arr.insert(i, new_entry)
                break
        else: # only executed if condition was never met
            arr.append(new_entry)    

def sorted_post_test():
    arr = []
    for _ in range(10000):
        arr.append(randrange(0, 100000))

    return sorted(arr)

def push_sorted_bs():
    arr = []
    for _ in range(10000):
        new_entry = randrange(0,100000)
        arr.insert(bisect_left(arr, new_entry), new_entry) 

def reverse_thes_pair(thesaurus, word, translation):
    if translation in thesaurus:
        thesaurus[translation].append(word)
    else:
        thesaurus[translation] = [word]

def reverse_thesaurus(thesaurus):
    rev_thes = {}
    for word, translations in thesaurus.items():
        for translation in translations:
            reverse_thes_pair(rev_thes, word, translation)
            rev_thes[translation] = sorted(rev_thes[translation])
    return rev_thes

def format_thesaurus(thesaurus):
    str_thes = ""
    for word, trans in thesaurus.items():
        str_thes += word
        str_thes += " - "
        str_thes += ", ".join(trans)
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
    print("All functionality with thesaurus from example:")
    print(format_thesaurus(reverse_thesaurus(read_file_thes('thesaurus.txt'))))

    t = Timer(lambda: push_sorted_old())
    print("My linear insert:", t.timeit(number=1))

    t = Timer(lambda: push_sorted_bs())
    print("Lib binary search insert:", t.timeit(number=1))
    
    t = Timer(lambda: sorted_post_test())
    print("Sorted:", t.timeit(number=1))

    unittest.main()