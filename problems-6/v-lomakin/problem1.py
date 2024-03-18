import random
import unittest

def randomSort(word):
    if len(word) > 2:
        mid = list(word[1:-1])
        random.shuffle(mid)
        return word[0] + ''.join(mid) + word[-1]
    else :
        return word

def alphabetSort(word):
    if len(word) > 2:
        mid = sorted(list(word[1:-1]))
        return word[0] + ''.join(mid) + word[-1]
    else :
        return word

def ranTextShuffle(string):
    word = ""
    res = ""
    for i in string:
        if i == ' ' :
            res += randomSort(word) + ' '
            word = ""
        else:
            word += i
    res += randomSort(word)
    return res

def alphTextShuffle(string):
    word = ""
    res = ""
    for i in string:
        if i == ' ' :
            res += alphabetSort(word) + ' '
            word = ""
        else:
            word += i
    res += alphabetSort(word)
    return res

print(ranTextShuffle("Это относительно большой текст с кучей воды и совершенно ненужных символов созданный исключительно с целью протестировать эти две функции написанные чтобы меня не исключили из этого учебного заведения"))

class TestFirstTask(unittest.TestCase):
    def test_word(self):
        self.assertEqual(alphTextShuffle("understand"),"uadennrstd") 
    def test_russian_alphabet(self):
        self.assertEqual(alphTextShuffle("Это относительно большой текст с кучей воды и совершенно ненужных символов созданный исключительно с целью протестировать эти две функции написанные чтобы меня не исключили из этого учебного заведения"),"Это оеилнносттьо блоошьй текст с кеучй вдоы и свеенноршо нежннуых свилмоов садзнноый иеикллнстчьюо с целью павеиооррсттть эти две фикнуци нааиннпсые чботы меня не иикллсчюи из эгото убгеночо завдееиня")
    def test_alphabet_empty(self):
        self.assertEqual(alphTextShuffle(""),"")
    def test_random_empty(self):
        self.assertEqual(ranTextShuffle(""),"")
    def test_random_length(self):
        self.assertEqual(len(ranTextShuffle("Это относительно большой текст с кучей воды и совершенно ненужных символов созданный исключительно с целью протестировать эти две функции написанные чтобы меня не исключили из этого учебного заведения")), len("Это относительно большой текст с кучей воды и совершенно ненужных символов созданный исключительно с целью протестировать эти две функции написанные чтобы меня не исключили из этого учебного заведения"))
    def test_random_short(self):
        self.assertEqual(ranTextShuffle("len"),"len")
if __name__ == '__main__':
    unittest.main()
