inputList = input().split()

l = len(inputList)
resultList = [None] * (l + 1)
resultList[0] = 0

for i in range(l):
    resultList[i+1] = resultList[i] + int(inputList[i])
    
print(resultList)