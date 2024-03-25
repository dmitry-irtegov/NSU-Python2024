
def green_bottles():
    result = ''
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']

    green_bottle = " green bottle"
    comma = ",\n"
    dot = ".\n"
    filler1 = " hanging on the wall"
    filler2_1 = "And if " 
    filler2_2 = green_bottle + " should accidentally fall"
    filler3_1 = "There'll be "
    filler4_1 = "If that "

    for i in range(len(numbers) - 1):
        if (i == (len(numbers) - 2)):
            result += numbers[i].title() + green_bottle + filler1 + comma
            result += numbers[i].title() + green_bottle + filler1 + comma
        else:
            result += numbers[i].title() + green_bottle + 's' + filler1 + comma
            result += numbers[i].title() + green_bottle + 's' + filler1 + comma

        if (i == (len(numbers) - 2)):
            result += filler4_1 + numbers[-2] + filler2_2
        else:    
            result += filler2_1 + numbers[-2] + filler2_2

        result += comma

        result += filler3_1 + numbers[i + 1] + green_bottle + 's' + filler1 + dot

    return result

def main():
    print(green_bottles())

main()