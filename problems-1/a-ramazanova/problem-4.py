def ten_green_bottles():
    numbers = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    for i in range(10):
        print(f'{numbers[i]} green bottles hanging on the wall,')
        print(f'{numbers[i]} green bottles hanging on the wall,')
        if i < 9:
            print('And if one green bottle should accidentally fall,')
            print(f'There’ll be {numbers[i + 1].lower()} green bottles hanging on the wall.')
        else:
            print('If that one green bottle should accidentally fall')
            print('There’ll be no green bottles hanging on the wall')


if __name__ == '__main__':
    ten_green_bottles()
