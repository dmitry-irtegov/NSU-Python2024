print("Enter sequence to search for")
sequence = input()
with open("pi.txt") as file:
    file_content = file.read()
    print(f'Found {file_content.count(sequence)} results')
    positions = ['0']
    for i in range(1, 6):
        found_position = file_content.find(sequence, int(positions[i - 1]) + 1)
        if found_position == -1:
            break
        positions.append(str(found_position))
    if len(positions) > 1:
        print(f'Positions: {" ".join(positions[1:6])} ...')
