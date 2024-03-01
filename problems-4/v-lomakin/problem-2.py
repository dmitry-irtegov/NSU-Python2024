#import argparse
import unittest

def tr(string, replace_from, replace_to, delete_chars=None):
    if len(replace_from) != len(replace_to):
        raise ValueError("Строки замены и заменяемые строки должны быть одинаковой длины")
    if len(replace_from) != len(set(replace_from)):
        raise ValueError("Заменяемые символы не должны повторяться")
    
    def translate_char(c):
        if delete_chars and c in delete_chars:
            return None
        try:
            index = replace_from.index(c)
            return replace_to[index]
        except ValueError:
            return c

    res = ""
    for i in string:
        ch = translate_char(i)
        if ch != None :
            res += ch
    return res

class TestTr (unittest.TestCase):
    def test_empty(self):
        self.assertEqual(tr("", "abc", "qwe", "ad"), "")

    def test_example(self):
        self.assertEqual(tr("abcd", "abc", "qwe", "ad"), "we")

    def test_error(self):
        with self.assertRaises(ValueError) as ve:
            tr("", "", "s")
        self.assertEqual(str(ve.exception), "Строки замены и заменяемые строки должны быть одинаковой длины")

    def test_error2(self):
        with self.assertRaises(ValueError) as ve:
            tr("", "bb", "se")
        self.assertEqual(str(ve.exception),"Заменяемые символы не должны повторяться") 

    def test_equal(self):
        self.assertEqual(tr("ex", "", ""), "ex")

    def test_equalArgs(self):
        self.assertEqual(tr("abcd", "abe", "abe"), "abcd")

    def test_deleteNothing(self):
        self.assertEqual(tr("abcd", "ab", "cd", ""), "cdcd")

    def test_oneLetter(self):
        self.assertEqual(tr("bbbbbbbbbbb", "b", "C"), "CCCCCCCCCCC")

#def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("replace_from", help="Строка символов для замены")
    #parser.add_argument("replace_to", help="Строка символов замены")
    #parser.add_argument("-d", "--delete", help="Список символов для удаления")
    #args = parser.parse_args()

    #string = input()
    #print(tr(string, args.replace_from, args.replace_to, args.delete))
        
if __name__ == "__main__":
    unittest.main()
    #main()
