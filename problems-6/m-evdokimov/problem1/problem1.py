import random
import argparse

def random_mix(word, length):
    word_list = list(word)
    letters = word_list[1:length-1]
    for index, letter in enumerate(word[1:length-1]):
        rand_index = random.randint(0, len(letters)-1)
        word_list[index+1] = (letters[rand_index])
        letters.pop(rand_index)
    return ''.join(word_list)
    

def abc_mix(word, length):
    word_list = list(word)
    letters = word_list[1:length-1]
    letters.sort(key = str.lower)
    for index, letter in enumerate(letters):
        word_list[index+1] = l
    return ''.join(word_list)
    

def mixer(string, mode, how_to_print = print):
    if mode == '' or mode is None:
        mode = 'random'
    if mode != 'abc' and mode != 'random':
        raise ValueError('Wrong mode name')
    
    for word in string.split():
        length = len(word)
        if length > 3:
            if mode == 'random':
                how_to_print(random_mix(word, length), end = ' ')
            if mode == 'abc':
                how_to_print(abc_mix(word, length), end = ' ')
        else:
            how_to_print(word, end = ' ')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_string", help="enter your input string here")
    parser.add_argument("-m", "--mode", help="choose mixer mode ('random' or 'abc')")
    args = parser.parse_args()
    mixer(args.input_string, args.mode) 