from collections import Counter
from io import StringIO

from letter_shuffler import LetterShuffler


class TestLetterShuffler:
    def test_no_letters(self):
        sample = '34 43522 432 !009 431'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: (_ for _ in ()).throw(Exception('Shuffling should not happen')), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == sample

    def test_one_letter(self):
        sample = '34f1 .'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: (_ for _ in ()).throw(Exception('Shuffling should not happen')), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == sample

    def test_two_letters(self):
        sample = '443 1гг 09'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: x.sort(), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == sample

    def test_three_letters(self):
        sample = 'abc 09'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: x.sort(), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == sample

    def test_letters_finish(self):
        sample = '432 s // абв'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: x.sort(), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == sample

    def test_sort_letters(self):
        sample = 'пульт от телевизора'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: x.sort(), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        assert output.getvalue() == 'плуьт от твеезилора'

    def test_shuffle_letters(self):
        sample = 'проверка'
        output = StringIO()
        shuffler = LetterShuffler(lambda x: x.sort(), output)
        for i in sample:
            shuffler.give_char(i)
        shuffler.finish()
        val = output.getvalue()
        assert val[0] == 'п'
        assert val[-1] == 'а'
        assert Counter(val) == Counter(sample)
