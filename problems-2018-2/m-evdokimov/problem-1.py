import sys

def wait_numeric():
    print("Please, enter a number")
    while True:
        try:
            string = input()
        except EOFError:
            print("EOF, goodbye.")
            break
            
        if is_number(string):
            print("You entered {string1}".format(string1 = string))
            break
        else:
            print("It's not a number\nPlease, enter a number")
            
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
        
if __name__ == "__main__":
    try:
      wait_numeric()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e, file=sys.stderr)