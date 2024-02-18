if __name__ == '__main__':
    bottle_count = ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    bottle_fall = '{} one green bottle should accidentally fall,'
    will_be = '{}{} green {} hanging on the wall{}'
    nothing = ''
    comma = ','
    for i in range(10):
        condition = "And if" if i != 9 else "If that"
        counts = "bottles" if i != 9 else "bottle"
        next_bottle_count = bottle_count[i + 1] if i != 9 else 'no'
        current_bottle_count = bottle_count[i]
        print(will_be.format(nothing, current_bottle_count, counts, comma))
        print(will_be.format(nothing, current_bottle_count, counts, comma))
        print(bottle_fall.format(condition))
        print(will_be.format('There’ll be ', str.lower(next_bottle_count), counts, '.'))
