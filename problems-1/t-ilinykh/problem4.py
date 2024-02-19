from num2words import num2words

def bottles(n):
    return f"{num2words(n, lang='en')} green bottle{'s' if n != 1 else ''}"

def main():
    for i in range(10, 0, -1):
        for j in range(2):
            print(f"{bottles(i).capitalize()} hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There’ll be {bottles(i-1) if i > 1 else 'no'} green bottle{'s' if i-1 != 1 else ''} hanging on the wall.\n")

if __name__ == "__main__":
    main()
