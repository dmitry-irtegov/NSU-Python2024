def number_to_words(num):
    words_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    return words_dict.get(num, str(num))

def bottles(n):
    if n == 1:
        return "One green bottle"
    else:
        return f"{number_to_words(n)} green bottles"

def main():
    for i in range(10, 0, -1):
        for j in range(2):
            print(bottles(i), "hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print("There’ll be ", end = '')
        if i == 1:
            print("no green bottles ", end = '')
        else:
            print(f"{bottles(i-1)} ", end = '')
        print("hanging on the wall. \n")

if __name__ == "__main__":
    main()
