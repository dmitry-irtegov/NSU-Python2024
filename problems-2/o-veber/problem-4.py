print("Enter sequence to search for")
sequence = input()
with open("pi.txt", 'r') as file:
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
