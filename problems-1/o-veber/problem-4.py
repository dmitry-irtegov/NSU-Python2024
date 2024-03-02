if __name__ == '__main__':
    bottle_count = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One', 'no']
    bottle_fall = '{} one green bottle should accidentally fall{}'
    will_be = '{}{} green {} hanging on the wall{}'
    nothing = ''
    comma = ','
    for i in range(10):
        condition = "And if" if i != 9 else "If that"
        counts = "bottles" if i != 9 else "bottle"
        comma_or_nothing = ',' if i != 9 else ''
        print(will_be.format(nothing, bottle_count[i], counts, comma))
        print(will_be.format(nothing, bottle_count[i], counts, comma))
        print(bottle_fall.format(condition, comma_or_nothing))
        print(will_be.format('There’ll be ', str.lower(bottle_count[i + 1]), 'bottles', '.'))
