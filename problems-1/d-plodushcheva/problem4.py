

def ten_green_bottles_song():
    nums = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "no"]
    for i in range(10):
        for _ in range(2):
            print(nums[i].title() + " green bottle" + ("s" if i != 9 else "")
                  + " hanging on the wall")
        print("And if one" + " green bottle" + " should accidentally fall")
        print("There’ll be " + nums[i + 1] + " green bottle" +
              ("s" if i != 8 else "") + " hanging on the wall")


if __name__ == '__main__':
    ten_green_bottles_song()
