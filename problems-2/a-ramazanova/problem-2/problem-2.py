import os
import sys
import traceback
import unittest


def make_dictionary(path):
    try:
        with open(path, 'r') as input_file:
            result = dict()
            for line in input_file.readlines():
                line = line.strip()
                word, translations = line.split(' - ')
                for translation in translations.split(', '):
                    if translation in result.keys():
                        result[translation].append(word)
                    else:
                        result[translation] = [word]
    except OSError as e:
        raise OSError('Error in reading file') from e
    try:
        with open(f'{path.replace(".txt", "")}_output.txt', 'w') as output_file:
            output_file.write('\n'.join(f'{word} - {", ".join(sorted(result[word]))}' for word in sorted(result)))
    except OSError as e:
        raise OSError('Error in writing file') from e


class TestWriteToFile(unittest.TestCase):
    def test1(self):
        data = "baca - fruit\nbacca - fruit\nmalum - apple, punishment\nmulta - punishment\npomum - apple\npopula - " \
               "apple\npopum - fruit"
        make_dictionary('test1.txt')

        self.assertTrue(os.path.exists('test1_output.txt'))

        with open('test1_output.txt', 'r') as f:
            self.assertEqual(f.read(), data)

    def test2(self):
        data = "t1 - w1\nt2 - w1, w2\nt3 - w1, w2, w3\nt4 - w1, w2, w3\nt5 - w2, w3\nt6 - w3"
        make_dictionary('test2.txt')

        self.assertTrue(os.path.exists('test2_output.txt'))

        with open('test2_output.txt', 'r') as f:
            self.assertEqual(f.read(), data)

    def test3(self):
        data = "t1 - w1"
        make_dictionary('test3.txt')

        self.assertTrue(os.path.exists('test3_output.txt'))

        with open('test3_output.txt', 'r') as f:
            self.assertEqual(f.read(), data)

    def test_exception(self):
        with self.assertRaises(OSError):
            make_dictionary('test4.txt')


if __name__ == '__main__':
    unittest.main()
