from sys import stderr


def open_file_and_count_lines():
    with open(filename, 'r') as file:
        buffer = ''
        line = file.readline()
        while line != '':
            line = line.replace('\n', '')
            buffer += line
            line = file.readline()
        character_found_count = buffer.count(sequence)
        print(f'Found {character_found_count} results')
        positions = ['-1']
        for i in range(1, 6):
            found_position = buffer.find(sequence, int(positions[i - 1]) + 1)
            if found_position == -1:
                break
            positions.append(str(found_position))
        if len(positions) > 1:
            many_dots_or_nothing = '...' if character_found_count > 5 else ''
            print(f'Positions: {" ".join(positions[1:6])}{many_dots_or_nothing}')


if __name__ == "__main__":
    print("Enter sequence to search for")
    filename = 'problem-4/pi.txt'
    sequence = input()
    try:
        open_file_and_count_lines()
    except FileNotFoundError:
        print(f"Tried to open file with name {filename}, but not found file with such name", file=stderr)
    except PermissionError:
        print(f"Tried to open file with name {filename}, but have no permission to do this action", file=stderr)
    except BaseException as e:
        print("Unexpected exception ", file=stderr)
        print(e, file=stderr)
