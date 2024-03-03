import unittest

def revers_dict(input_dict):
    output_dict = {}

    for english, latin_words in input_dict.items():
        for latin in latin_words:
            if latin in output_dict:
                output_dict[latin].append(english)
            else:
                output_dict[latin] = [english]
                
    sorted_dict = {key: output_dict[key] for key in sorted(output_dict)}
    return sorted_dict

def read_dict_file(file_path):
    input_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            english, latin_translations = line.strip().split(' - ')
            input_dict[english] = latin_translations.split(', ')
    return input_dict
    
def print_dict(some_dict):
    for english, latin_words in some_dict.items():
        print(english, end = " - ")
        for latin in latin_words[:-1]:
            print(latin, end = ", ")
        if latin_words: 
            print(latin_words[-1])
   
latin_english_dict = revers_dict(read_dict_file('input_task_2.txt'))
print_dict(latin_english_dict)

inp_dict = {'fruit': []}
prog_ans = revers_dict(inp_dict)
print_dict(prog_ans)

###

class TestDictRevers(unittest.TestCase):
    def test_examples(self):
        prog_ans = revers_dict(read_dict_file('input_task_2.txt'))
        correct_ans = {
            'baca': ['fruit'],
            'bacca': ['fruit'],
            'malum': ['apple', 'punishment'],
            'mult': ['punishment'],
            'pomum': ['apple'],
            'popula': ['apple'],
            'mult': ['punishment'],
            'popum': ['fruit'],
            }
        self.assertEqual(prog_ans, correct_ans)
    def test_empty(self):
        inp_dict = {}
        correct_ans = {}
        prog_ans = revers_dict(inp_dict)
        self.assertEqual(prog_ans, correct_ans)
    def test_empty_translate(self):
        inp_dict = {'fruit': []}
        correct_ans = {}
        prog_ans = revers_dict(inp_dict)
        self.assertEqual(prog_ans, correct_ans)
        


if __name__ == '__main__':
    unittest.main()
    
