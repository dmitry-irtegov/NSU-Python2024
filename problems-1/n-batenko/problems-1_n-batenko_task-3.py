
def collatz_conjecture():
    num = int(input("Provide any integer: "))
    temp = num
    seq = [num]

    while temp != 1:
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = 3 * temp + 1
        seq.append(temp)
    
    return seq

def collatz_printer(seq):
    result = ''
    for i in range(len(seq)):
        result += str(seq[i])
        if i != (len(seq) - 1):
            result += ' -> '
    
    return result

def main():
    print(collatz_printer(collatz_conjecture()))

main()