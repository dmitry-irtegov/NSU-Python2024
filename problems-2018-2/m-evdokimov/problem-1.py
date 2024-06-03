def wait_numeric():
    print("Please, enter a number")
    string = input()
    if string.isnumeric():
        print("You entered {string1}".format(string1 = string))
    else:
        print("It's not a number")
        wait_numeric()
        
if __name__ == "__main__":
  wait_numeric()