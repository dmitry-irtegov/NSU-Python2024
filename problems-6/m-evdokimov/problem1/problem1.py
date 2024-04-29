import random
import argparse
import re

def random_mix(word, length):
    word_list = list(word)
    letters = word_list[1:length-1]
    for index, l in enumerate(word[1:length-1]):
        rand_index = random.randint(0, len(letters)-1)
        word_list[index+1] = (letters[rand_index])
        letters.pop(rand_index)
    return ''.join(word_list)
    

def abc_mix(word, length):
    letters = list(word)[1:length-1]
    letters.sort(key = str.lower)
    return word[0] + ''.join(letters) + word[-1]

def preprocessing(word):
    letters = re.search(r'\w+', word)
    punct_start = re.search(r'\W+\b', word)
    punct_end = re.search(r'\b\W+', word)
    
    if punct_start == None:
        punct_start = ''
    else:
        punct_start = punct_start[0]
        
    if punct_end == None:
        punct_end = ''
    else:
        punct_end = punct_end[0]
        
    return punct_start, punct_end, letters[0]

def mixer(string, mode, how_to_print = print):
    if mode == '' or mode is None:
        mode = 'random'
    if mode != 'abc' and mode != 'random':
        raise ValueError('Wrong mode name')
    
    if mode == 'random':
        for word in string.split():
            p_start, p_end, word = preprocessing(word)
            length = len(word)
            if length > 3:
                how_to_print(p_start, random_mix(word, length), p_end, sep = '', end = ' ')
            else:
                how_to_print(p_start, word, p_end, sep = '', end = ' ')
                
    if mode == 'abc':
        for word in string.split():
            p_start, p_end, word = preprocessing(word)
            length = len(word)
            if length > 3:
                how_to_print(p_start, abc_mix(word, length), p_end, sep = '', end = ' ')
            else:
                how_to_print(p_start, word, p_end, sep = '', end = ' ')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_string", help="enter your input string here")
    parser.add_argument("-m", "--mode", help="choose mixer mode ('random' or 'abc')")
    args = parser.parse_args()
    mixer(args.input_string, args.mode)