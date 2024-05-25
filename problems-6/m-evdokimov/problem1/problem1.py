import random
import argparse
import re
import sys

def random_mix(word, length):
    word_list = list(word)
    letters = word_list[1:length-1]
    for index, letter in enumerate(word[1:length-1]):
        rand_index = random.randint(0, len(letters)-1)
        word_list[index+1] = (letters[rand_index])
        letters.pop(rand_index)
    return ''.join(word_list)
    

def abc_mix(word, length):
    letters = list(word)[1:length-1]
    letters.sort(key = str.lower)
    return word[0] + ''.join(letters) + word[-1]

def mix(mix_type, string):
    for match in re.finditer(r'\w+', string):
        index_start = match.start()
        index_end = match.end()
        word = match[0]
        length = len(word)
        if length > 3:
            string = string[:index_start] + mix_type(word, length) + string[index_end:]
    return string

def mixer(string, mode, how_to_print = print):
    if mode == '' or mode is None:
        mode = 'random'
    if mode != 'abc' and mode != 'random':
        raise ValueError('Error: Wrong mode name')
    
    if mode == 'random':
        string = mix(random_mix, string)     
                
    if mode == 'abc':
        string = mix(abc_mix, string)
            
    how_to_print(string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_string", help="enter your input string here")
    parser.add_argument("-m", "--mode", help="choose mixer mode ('random' or 'abc')")
    args = parser.parse_args()
    try:
        mixer(args.input_string, args.mode)
    except Exception as e:
        print(e, file=sys.stderr)