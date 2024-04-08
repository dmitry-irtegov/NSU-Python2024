def print_lyrics():
    numbers = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one', 'no']
    for index, num in enumerate(numbers):
        for _ in range(2):
            print(num.title(), " bottle", "s" if num != "one" else "", " hanging on the wall,", sep="")
        print("And if" if num != "one" else "If that", "one green bottle should accidentally fall,")
        print("There’ll be ", numbers[index + 1], " green bottle",
              "s" if numbers[index + 1] != "one" else "", " hanging on the wall.", sep="")
        if num == "one":
            break


print_lyrics()
