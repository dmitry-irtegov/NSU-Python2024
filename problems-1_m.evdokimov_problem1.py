inputList = input().split()

resultList = [0]
for i in range(len(inputList)):
    resultList.append(resultList[i] + int(inputList[i]))
print(resultList)