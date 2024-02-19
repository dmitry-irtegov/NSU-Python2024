n = int(input())

i = 2
resList = []
while i * i <= n:
    while n % i == 0:
        resList.append(i)
        n = n // i
    i = i + 1
if n > 1:
    resList.append(n)
    
setList = set(resList)
final = []
for i in setList:
    final.append([i, resList.count(i)])
    
print(final)
