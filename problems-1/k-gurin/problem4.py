# problems-1/assignment-4
def ten_green_bottles():
    num = ["ten", "nine", "eight", "seven", "six",
           "five", "four", "three", "two", "one", "no"]
    sentence_1 = " green bottles hanging on the wall,"
    sentence_2 = " green bottle hanging on the wall,"
    sentence_3 = " one green bottle should accidentally fall,"
    sentence_4 = "There’ll be "
    for i in range(10):
        print(num[i].capitalize() + (sentence_1 if i != 9 else sentence_2))
        print(num[i].capitalize() + (sentence_1 if i != 9 else sentence_2))
        print(("And if" if i != 9 else "If that") + sentence_3)
        print(sentence_4 + num[i + 1] + (sentence_2 if i == 8 else sentence_1))


ten_green_bottles()
