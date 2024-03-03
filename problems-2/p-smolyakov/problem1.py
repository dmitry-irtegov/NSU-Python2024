#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    while True:
        try:   
            user_text = input('Type some integer value: ')
        except EOFError:
            print('~ An integer still hasn\'t been typed, but no more input is coming. Exiting.')
            sys.exit(1)

        try:
            num = int(user_text)
        except ValueError:
            print(f'{user_text} is not an integer value! Try again.')
        else:
            print(f'You typed {num}. Congratulations!')
            sys.exit(0)
