def wait_numeric():
    print("Please, enter a number")
    while True:
        string = input()
        if string.isnumeric():
            print("You entered {string1}".format(string1 = string))
            break
        else:
            print("It's not a number")
            print("Please, enter a number")
        
if __name__ == "__main__":
  wait_numeric()