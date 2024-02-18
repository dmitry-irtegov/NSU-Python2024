

def ten_green_bottles_song():
    numbers = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "no"]
    s1 = "green bottles hanging on the wall,"
    s2 = "And if one green bottle should accidentally fall,"
    s3 = "There’ll be green bottles hanging on the wall."
    for i in range(9):
        print(numbers[i].title(), s1)
        print(numbers[i].title(), s1)
        print(s2)
        if i == 8:
            print(s3[:11], numbers[i + 1], s3[12:24], s3[26:])
        else:
            print(s3[:11], numbers[i + 1], s3[12:])
    print(numbers[9].title(), " ", s1[:12], s1[13:], sep='')
    print(numbers[9].title(), " ", s1[:12], s1[13:], sep='')
    print("If that", s2[7:])
    print(s3[:11], numbers[10], s3[12:])


if __name__ == '__main__':
    ten_green_bottles_song()
