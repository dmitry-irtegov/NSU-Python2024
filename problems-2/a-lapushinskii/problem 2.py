import unittest
import sys

def revers_dict(input_dict):
    output_dict = {}

    for english, latin_words in input_dict.items():
        for latin in latin_words:
            if latin in output_dict:
                output_dict[latin].append(english)
            else:
                output_dict[latin] = [english]
                
    return output_dict

def read_dict_file(file_path):
    try:
        input_dict = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                english, latin_translations = line.strip().split(' - ')
                input_dict[english] = latin_translations.split(', ')
        return input_dict
    except Exception as e:
        print("Ошибка при открытии файла: ", e, file=sys.stderr)
        return {}
    
def print_dict_to_file(some_dict, filename):
    sorted_dict = dict(sorted(some_dict.items()))
    try:
        with open(filename, 'w') as file:
            for english, latin_words in sorted_dict.items():
                file.write(f"{english} - ")
                for latin in latin_words[:-1]:
                    file.write(f"{latin}, ")
                if latin_words: 
                    file.write(f"{latin_words[-1]}\n")
    except Exception as e:
        print("Ошибка при сохранении результата: ", e, file=sys.stderr)
        return {}
   
latin_english_dict = revers_dict(read_dict_file('inpt_task_2.txt'))
print_dict_to_file(latin_english_dict, 'output_task_2.txt')

###

class TestDictRevers(unittest.TestCase):
    def test_examples(self):
        prog_ans = revers_dict(read_dict_file('input_task_2.txt'))
        correct_ans = {
            'baca': ['fruit'],
            'bacca': ['fruit'],
            'malum': ['apple', 'punishment'],
            'multa': ['punishment'],
            'pomum': ['apple'],
            'popula': ['apple'],
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
    
