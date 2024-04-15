"""
This module contains functions to search for a sequence of digits in the digits of pi.
"""

def find_sequence(sequence, pi_file):
    """
    Find all occurrences of a sequence of digits in the digits of pi.

    Args:
    sequence (str): The sequence of digits to search for.
    pi_file (str): The path to the file containing the digits of pi.

    Returns:
    list: A list of positions where the sequence was found.
    """
    positions = []
    with open(pi_file, 'r', encoding='utf-8') as f:
        buffer = ''
        for l in f:
            l = l.replace('\n', '')
            buffer += l
        start = 0
        while True:
            pos = buffer.find(sequence, start)
            if pos == -1:
                break
            positions.append(pos)
            start = pos + 1
    return positions

def main():
    """
    Main function to execute the program.
    """
    pi_file = 'pi.txt'
    print("Enter sequence to search for:")
    sequence = input("> ")
    positions = find_sequence(sequence, pi_file)
    print(f"Found {len(positions)} results.")
    print("Positions:", ' '.join(map(str, positions[:5])))

if __name__ == "__main__":
    main()
