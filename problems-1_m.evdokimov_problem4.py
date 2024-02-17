numberList = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
wall = 'green bottles hanging on the wall'
andif = 'And if one green bottle should accidentally fall'
will = 'There’ll be'

for i in range(9):
    for j in range(2):
        print(numberList[10-i][0].upper(), numberList[10-i][1:], ' ', wall, sep = '')
    print(andif)
    if i == 8:
        print(will, ' ', numberList[10-i-1], ' ', wall[:12], wall[13:], sep = '')
    else:
        print(will, numberList[10-i-1], wall)

for j in range(2):
    print(numberList[1][0].upper(), numberList[1][1:], ' ', wall[:12], wall[13:], sep = '')
print('If that one green bottle should accidentally fall')
print(will, numberList[0], wall)
