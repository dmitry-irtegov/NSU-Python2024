import sys


BLOCK_SIZE = 10000  # Reading 10,000 characters at a time

def find_sequence(sequence):
    indexes = []
    offset = len(sequence) - 1

    with open("pi.txt", "r") as file:
        block = ""
        for line in file:
            block += line.strip("\n")
            if len(block) >= BLOCK_SIZE:
                find_sequence_in_block(block, sequence, indexes)
                block = block[-offset:]
        find_sequence_in_block(block, sequence, indexes)

    return indexes


def find_sequence_in_block(block, sequence, indexes):
    index = block.find(sequence)
    while index != -1:
        indexes.append(index)
        index = block.find(sequence, index + 1)


if __name__ == "__main__":
    try:
        while True:
            sequence = input("Enter sequence to search for.\n> ")
            sequence_indexes = find_sequence(sequence)
            print(f"Found {len(sequence_indexes)} results")
            print(f"Positions: {sequence_indexes}")
    except EOFError:
        exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}")
        exit(1)
