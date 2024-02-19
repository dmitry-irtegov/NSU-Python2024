num = input("Enter number. \n> ")
num = int(num)
result = "" + str(num)
while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    result += " -> " + str(num)
print(result)


