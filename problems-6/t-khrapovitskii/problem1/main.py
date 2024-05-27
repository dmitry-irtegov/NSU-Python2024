import random

from letter_shuffler import LetterShuffler

if __name__ == '__main__':
    try:
        with open('text.txt', 'r', encoding='utf-8') as original:
            try:
                with open('shuffled.txt', 'w', encoding='utf-8') as shuffle:
                    shuffler1 = LetterShuffler(random.shuffle, shuffle)
                    while True:
                        try:
                            char = original.read(1)
                        except Exception as e:
                            print("Error when reading from text.txt\n" + str(e))
                            exit(1)
                        if char == '':
                            break
                        try:
                            shuffler1.give_char(char)
                        except Exception as e:
                            print("Error when writing to shuffled.txt\n" + str(e))
                            exit(1)
            except Exception as e:
                print("Error when opening shuffled.txt\n" + str(e))
                exit(1)

            try:
                original.seek(0)
            except Exception as e:
                print("Error when seeking text.txt\n" + str(e))
                exit(1)
            try:
                with open('sorted.txt', 'w', encoding='utf-8') as sort:
                    shuffler2 = LetterShuffler(lambda x: x.sort(), sort)
                    while True:
                        try:
                            char = original.read(1)
                        except Exception as e:
                            print("Error when reading from text.txt\n" + str(e))
                            exit(1)
                        if char == '':
                            break
                        try:
                            shuffler2.give_char(char)
                        except Exception as e:
                            print("Error when writing to sorted.txt\n" + str(e))
                            exit(1)
            except Exception as e:
                print("Error when opening sorted.txt\n" + str(e))
                exit(1)
    except Exception as e:
        print("Error when opening text.txt\n" + str(e))
        exit(1)
