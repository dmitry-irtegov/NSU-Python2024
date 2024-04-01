
def green_bottles():
    result = ''
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']

    green_bottle = " green bottle"
    comma = ",\n"
    dot = ".\n"
    hanging_on_the_wall = " hanging on the wall"
    and_if = "And if " 
    green_bottle_should_accidentally_fall = green_bottle + " should accidentally fall"
    threre_ll_be = "There'll be "
    if_that = "If that "

    for i in range(len(numbers) - 1):
        for _ in range(2):
            result += numbers[i].title() + green_bottle
            
            if (i != (len(numbers) - 2)):
                result += "s"
                
            result += hanging_on_the_wall + comma

        if (i == (len(numbers) - 2)):
            result += if_that
        else:    
            result += and_if

        result += numbers[-2] + green_bottle_should_accidentally_fall

        result += comma

        result += threre_ll_be + numbers[i + 1] + green_bottle + 's' + hanging_on_the_wall + dot

    return result

def main():
    print(green_bottles())

main()