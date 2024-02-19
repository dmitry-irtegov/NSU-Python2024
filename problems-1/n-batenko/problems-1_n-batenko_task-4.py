
def green_bottles():
    result = ''
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']

    green_bottle = "green bottle"
    all = "all,"
    filler1 = " " + green_bottle + "s hanging on the w"
    filler2_1 = "And if " 
    filler2_2 = " " + green_bottle + " should accidentally f"
    filler3_1 = "There'll be "
    filler4_1 = "If that "

    for i in range(len(numbers) - 1):
        result += numbers[i].title() + filler1 + all
        result += numbers[i].title() + filler1 + all

        if (i == (len(numbers) - 1)):
            result += filler4_1 + numbers[-2] + filler2_2 + all
        else:    
            result += filler2_1 + numbers[-2] + filler2_2 + all

        result += filler3_1 + numbers[i + 1] + filler1 + all
    
    return result

def main():
    print(green_bottles())

main()