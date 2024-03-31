import sys

PI_FILENAME = "pi.txt"
SEQUENCE_MULTIPLIER = 10


def search_sequence(sequence: str):
    indexes = []
    block_index = 0
    offset = len(sequence) - 1
    block_size = SEQUENCE_MULTIPLIER * len(sequence)
    block = ""
    with open(PI_FILENAME, "r") as file:
        for line in file:
            block = block + line.strip("\n")
            if len(block) < block_size:
                continue
            index = block.find(sequence)
            while index != -1:
                indexes.append(block_index + index - 2)
                index = block.find(sequence, index + 1, len(block))

            block_index += len(block) - offset
            block = block[-offset:]
    return indexes


if __name__ == "__main__":
    try:
        substring = input("Enter sequence to search for.\n> ")
        while True:
            sequence_indexes = search_sequence(substring)
            print(f"Found {len(sequence_indexes)} results")
            print(f"Positions: {sequence_indexes}")
            substring = input("Enter sequence to search for.\n> ")
    except EOFError as e:
        exit(0)
    except Exception as e:
        sys.stderr.write(f"Error while searching sequence \"{substring}\": {str(e)}")
        exit(1)
