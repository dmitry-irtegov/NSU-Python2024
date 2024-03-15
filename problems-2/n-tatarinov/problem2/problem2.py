import unittest

def to_lat_eng(filename):
    translations = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            eng, latin = line.rstrip().split(' - ')
            for word in latin.split(', '):
                if word in translations:
                    translations[word].append(eng)
                else:
                    translations[word] = [eng]
    for key in translations:
        translations[key].sort()
        translations[key] = ', '.join(translations[key])
    res = [0] * len(translations)
    i = 0
    for key in translations:
        res[i] = f'{key} - {translations[key]}'
        i += 1
    res.sort()
    return res

class TestLatEngDictionary(unittest.TestCase):
    def test_dictionary_from_task(self):
        lat_eng = to_lat_eng('problems-2/n-tatarinov/problem2/dictionary.txt')
        self.assertEqual(lat_eng[0], 'baca - fruit')
        self.assertEqual(lat_eng[1], 'bacca - fruit')
        self.assertEqual(lat_eng[2], 'malum - apple, punishment')
        self.assertEqual(lat_eng[3], 'multa - punishment')
        self.assertEqual(lat_eng[4], 'pomum - apple')
        self.assertEqual(lat_eng[5], 'popula - apple')
        self.assertEqual(lat_eng[6], 'popum - fruit')

if __name__ == '__main__':
    unittest.main()