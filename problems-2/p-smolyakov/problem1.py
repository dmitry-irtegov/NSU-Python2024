#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    while True:
        try:   
            user_text = input('Type some integer value: ')
        except EOFError:
            print('\nEnd of input file. Exiting.', file=sys.stderr)
            sys.exit(1)
        except KeyboardInterrupt:
            print('\nSIGINT received. Exiting.', file=sys.stderr)
            sys.exit(1)
        except BaseException as e:
            print(f'\nMet {repr(e)} while reading from stdin. Exiting.', file=sys.stderr)
            sys.exit(1)

        try:
            num = int(user_text)
        except ValueError:
            print(f'\n{user_text} is not an integer value! Try again.', file=sys.stderr)
        else:
            print(f'\nYou typed {num}. Congratulations!')
            sys.exit(0)
