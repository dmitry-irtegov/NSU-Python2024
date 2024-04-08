from sys import stderr


def open_file_and_count_lines():
    with open(filename, 'r') as file:
        buffer = ''
        for line in file:
            line = line.replace('\n', '')
            buffer += line
        character_found_count = buffer.count(sequence)
        print(f'Found {character_found_count} results')
        positions = []
        for i in range(5):
            if i == 0:
                found_position = buffer.find(sequence)
            else:
                found_position = buffer.find(sequence, positions[i - 1] + 1)
            if found_position == -1:
                break
            positions.append(found_position)
        if len(positions) > 0:
            many_dots_or_nothing = '...' if character_found_count > 5 else ''
            print(f'Positions: {" ".join(map(str, positions))}{many_dots_or_nothing}')


if __name__ == "__main__":
    print("Enter sequence to search for")
    filename = 'pi.txt'
    sequence = input()
    try:
        open_file_and_count_lines()
    except BaseException as e:
        print("Unexpected exception ", e, file=stderr)
