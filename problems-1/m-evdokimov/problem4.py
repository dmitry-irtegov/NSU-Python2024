import unittest

t_o = []

def custom_print(*ins, **args):
    t_o.append(''.join(ins))

def song():

    numberList = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    letter_s = 's'
    green = 'green bottle'
    wall = 'hanging on the wall'
    andif = 'And if one green bottle should accidentally fall'
    will = 'There’ll be'
    ifThat = 'If that one green bottle should accidentally fall'

    for i in range(9):
        for j in range(2):
            print(numberList[10-i][0].upper(), numberList[10-i][1:], ' ', green, letter_s, ' ', wall, sep = '')
        print(andif)
        if i == 8:
            print(will, ' ', numberList[10-i-1], ' ', green, ' ', wall)
        else:
            print(will, ' ', numberList[10-i-1], ' ', green, letter_s, ' ', wall, sep = '')

    for j in range(2):
        print(numberList[1][0].upper(), numberList[1][1:], ' ', green, ' ', wall, sep = '')
    print(ifThat)
    print(will, ' ', numberList[0], ' ', green, letter_s, ' ', wall, sep = '')
    
class TestSong(unittest.TestCase):
    
    def setUp(self):
        global print
        self.orig_print = print
        print = custom_print
        t_o.clear()

    def tearDown(self):
        global print
        print = self.orig_print
  
    def test_song(self):
        song()
        self.assertEqual(t_o, 
['Ten green bottles hanging on the wall',
'Ten green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be nine green bottles hanging on the wall',
'Nine green bottles hanging on the wall',
'Nine green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be eight green bottles hanging on the wall',
'Eight green bottles hanging on the wall',
'Eight green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be seven green bottles hanging on the wall',
'Seven green bottles hanging on the wall',
'Seven green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be six green bottles hanging on the wall',
'Six green bottles hanging on the wall',
'Six green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be five green bottles hanging on the wall',
'Five green bottles hanging on the wall',
'Five green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be four green bottles hanging on the wall',
'Four green bottles hanging on the wall',
'Four green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be three green bottles hanging on the wall',
'Three green bottles hanging on the wall',
'Three green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be two green bottles hanging on the wall',
'Two green bottles hanging on the wall',
'Two green bottles hanging on the wall',
'And if one green bottle should accidentally fall',
'There’ll be one green bottle hanging on the wall',
'One green bottle hanging on the wall',
'One green bottle hanging on the wall',
'If that one green bottle should accidentally fall',
'There’ll be no green bottles hanging on the wall'])
  
if __name__ == "__main__":
    unittest.main()
    #print(t_o)