import unittest
result = ""

def myPrint(x, **kvarg):
    global result
    if isinstance(x, str):
        result = result + x

origPrint = print
print = myPrint

def findPos (sub):
    with open('pi.txt', 'r') as file:
        pi = ''.join(line.strip() for line in file)
    list = []
    x = pi.find(sub)
    while (x != -1):
        list.append(x - 1)
        x = pi.find(sub, x+1)
    cnt = len(list)
    print(f"Found {cnt} results.\n")
    if cnt < 5 :
        print(f"Positions: {list}\n")
    else :
        newList = []
        for i in list[:5]:
            newList.append(i)
        print(f"Positions: {newList}\n")
        
    file.close()
    return list

class TestsFindPosition(unittest.TestCase):
    def test_qwerty(self):
        global result
        findPos("123456")
        self.assertEqual(result,"Found 2 results.\nPositions: [2458885, 3735793]\n")
        origPrint(result)
        result = ""

    def test_five(self):
        global result
        findPos("10049")
        self.assertEqual(result,"Found 49 results.\nPositions: [81181, 81663, 164755, 166002, 227951]\n")
        origPrint(result)
        result = ""

    def test_one(self):
        global result
        findPos("1")
        self.assertEqual(result,"Found 419139 results.\nPositions: [1, 3, 37, 40, 49]\n")
        origPrint(result)
        result = ""

if __name__ == '__main__':
    unittest.main()
    origPrint(result)
