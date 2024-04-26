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
        word_list[index+1] = letter
    return ''.join(word_list)

def preprocessing(word):
    begin_index = 0
    punctuations_start = ''
    while not word[begin_index].isalpha():
        begin_index = begin_index + 1
    if begin_index > 0:
        punctuations_start = word[0:begin_index]
        word = word[begin_index:]
    end_index = 0
    punctuations_end = ''
    length = len(word)
    while end_index < length and word[end_index].isalpha():
        end_index = end_index + 1
    if end_index != len(word):
        punctuations_end = word[end_index:]
        word = word[0:end_index]
    return punctuations_start, punctuations_end, word

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