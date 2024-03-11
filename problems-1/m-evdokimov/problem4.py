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
        print(will, numberList[10-i-1], green, wall)
    else:
        print(will, ' ', numberList[10-i-1], ' ', green, letter_s, ' ', wall, sep = '')

for j in range(2):
    print(numberList[1][0].upper(), numberList[1][1:], ' ', green, ' ', wall, sep = '')
print(ifThat)
print(will, ' ', numberList[0], ' ', green, letter_s, ' ', wall, sep = '')