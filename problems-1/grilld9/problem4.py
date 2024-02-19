templ_wall = " green bottles hanging on the wall"
templ_fall = "And if one green bottle should accidentally fall,\n"
templ_will = "There’ll be "
amounts = ["Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One", "no"]
amounts_low_case = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "no"]
result = ""
for i in range(0, 10):
    result += amounts[i] + templ_wall + ",\n"
    result += amounts[i] + templ_wall + ",\n"
    result += templ_fall
    result += templ_will + amounts_low_case[i + 1] + templ_wall + ".\n"
print(result)