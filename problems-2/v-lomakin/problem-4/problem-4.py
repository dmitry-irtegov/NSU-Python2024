import unittest

def findPos (sub):
    file = open('pi.txt', "r")
    pi = ''.join([a.replace("\n", "") for a in file.readlines()])
    list = []
    x = pi.find(sub)
    while (x != -1):
        list.append(x - 1)
        x = pi.find(sub, x+1)
    file.close()
    return list

class TestsFindPosition(unittest.TestCase):
    def test_qwerty(self):
        self.assertEqual(findPos("123456"),[2458885,3735793])   

    def test_five(self):
        self.assertEqual(findPos("10049"),[81181, 81663, 164755, 166002, 227951, 382558, 432784, 544247, 556921, 576840, 587404, 605735, 683581, 801882, 810013, 916813, 965597, 1338969, 1501899, 1659357, 1816026, 1951287, 1979822, 2083050, 2119932, 2134021, 2140467, 2166789, 2297621, 2558072, 2571475, 2581813, 2636173, 2668633, 2745051, 2850004, 2854857, 2867894, 2887618, 3059735, 3100890, 3457720, 3506380, 3547206, 3634950, 3819063, 3918388, 4074393, 4191306])

if __name__ == '__main__':
    unittest.main()
