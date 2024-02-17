inputList = input().split()
a, b = input().split()
a = int(a)
b = int(b)

resultList = []
for i in inputList:
    x = int(i)
    if x > b:
        x = b
    if x < a:
        x = a
    resultList.append(x)
    
print(resultList)
