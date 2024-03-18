def find_sequence(sequence, content):
    positions = []
    start_index = 0
    while True:
        index = content.find(sequence, start_index)
        if index == -1:
            break
        positions.append(index)
        start_index = index + 1
    return positions

def main():
    with open('pi.txt', 'r') as file:
        pi_content = file.read()

    while True:
        sequence = input("Enter sequence to search for.\n")
        positions = find_sequence(sequence, pi_content)
        num_occurrences = len(positions)
        print(f"Found {num_occurrences} results.")
        print("Positions:", " ".join(map(str, positions[:5])))

        if num_occurrences == 0:
            break

if __name__ == "__main__":
    main()
