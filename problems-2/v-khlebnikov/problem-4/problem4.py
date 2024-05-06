import unittest

BLOCK_SIZE = 12345


def print_pi_positions(positions):
    count = len(positions)
    print(f"Found {count} results.")
    if count > 0:
        print(f"Positions: {positions[0]} ", end="")
        internal_counter = 1
        while internal_counter < 5 and count - internal_counter > 0:
            print(positions[internal_counter], end=" ")
            internal_counter += 1
        if count > 5:
            print("...", end="")
        print()


def find_positions_in_block(block, positions, substring, lower_bound):
    index = block.find(substring)
    while index != -1:
        positions.append(index + lower_bound)
        index = block.find(substring, index + 1)


def find_positions_in_pi(substring, file_path):
    positions = []
    offset = len(substring) - 1

    try:
        file = open(file_path, "r")
    except FileNotFoundError as e:
        e.strerror = f"File '{file_path}' not found: " + e.strerror
        raise e
    except PermissionError as e:
        e.strerror = f"Cannot access file '{file_path}': permission denied: " + e.strerror
        raise e
    except IsADirectoryError as e:
        e.strerror = f"Cannot open file '{file_path}': cause it's a directory: " + e.strerror
        raise e
    except Exception as e:
        e.strerror = "Caught unhandled exception while execution: " + e.strerror
        raise e
    with file:
            try:
                block = ""
                lower_bound = 0
                for line in file:
                    block += line.strip()
                    if len(block) >= BLOCK_SIZE:
                        find_positions_in_block(block, positions, substring, lower_bound)
                        lower_bound += len(block) - offset
                        block = block[-offset:]
                find_positions_in_block(block, positions, substring, lower_bound)
            except IOError as e:
                e.strerror = f"Cannot open file '{file_path}': cause it's a directory: " + e.strerror
                raise e

    return positions


class TestPiFinder(unittest.TestCase):

    def test_first(self):
        positions = find_positions_in_pi("123", 'pi.txt')
        self.assertEqual(4185, len(positions))
        self.assertEqual([1923, 2937, 2975, 3891, 6547], positions[:5])

    def test_second(self):
        positions = find_positions_in_pi("1415", 'pi.txt')
        self.assertEqual(424, len(positions))
        self.assertEqual([0, 6954, 29135, 45233, 79686], positions[:5])

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            find_positions_in_pi("123", "123")
    

if __name__ == '__main__':
    unittest.main()
