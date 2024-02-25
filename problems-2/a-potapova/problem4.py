PI_FILENAME = "pi.txt"


def search_sequence(sequence: str):
    indexes = []
    block_index = 0
    offset = len(sequence) - 1
    with open(PI_FILENAME, "r") as file:
        line = file.readline().strip("\n")
        while len(line) != offset:
            index = line.find(sequence)
            while index != -1:
                indexes.append(block_index + index - 2)
                index = line.find(sequence, index + 1, len(line))
            block_index += len(line) - offset
            line = line[-offset:] + file.readline().strip("\n")
    return indexes


if __name__ == "__main__":
    sequence_indexes = search_sequence(input("Enter sequence to search for.\n > "))
    print(f"Found {len(sequence_indexes)} results")
    print(f"Positions: {sequence_indexes}")
