inputList = input().split()
a, b = input().split()
a = int(a)
b = int(b)

resultList = [None] * len(inputList)
for i in range(len(inputList)):
    x = int(inputList[i])
    if x > b:
        x = b
    if x < a:
        x = a
    resultList[i] = x
    
print(resultList)