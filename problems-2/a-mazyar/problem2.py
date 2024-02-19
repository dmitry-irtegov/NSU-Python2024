import unittest
import re
from timeit import Timer
from bisect import bisect_left

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

def push_sorted_old(arr, new_entry):
    if arr:
        for i, entry in enumerate(arr):
            if new_entry < entry:
                arr.insert(i, new_entry)
                return
    
    arr.append(new_entry)

def sorted_post_test():
    arr = []
    for x in range(10000):
        arr.append(x)

    return sorted(arr)

def push_sorted(arr, new_entry):
    arr.insert(bisect_left(arr, new_entry), new_entry)

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

    test_arr = []
    t = Timer(lambda: [push_sorted_old(test_arr, x) for x in range(10000)])
    print("My linear insert:", t.timeit(number=1))

    test_arr = []
    t = Timer(lambda: [push_sorted(test_arr, x) for x in range(10000)])
    print("Lib binary search insert:", t.timeit(number=1))
    
    t = Timer(lambda: sorted_post_test())
    print("Sorted:", t.timeit(number=1))

    unittest.main()