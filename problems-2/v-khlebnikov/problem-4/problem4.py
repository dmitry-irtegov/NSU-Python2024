import sys
import unittest


def print_pi_positions(counter, positions):
    print(f"Found {counter} results.")
    if counter > 0:
        print(f"Positions: {positions[0]} ", end="")
        internal_counter = 1
        while internal_counter < 5 and counter - internal_counter > 0:
            print(positions[internal_counter], end=" ")
            internal_counter += 1
        if counter > 5:
            print("...", end="")
        print()


def find_positions_in_pi(x, file_path):
    counter = 0
    answers = [0] * 5
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        print(f"File '{file_path}' not found", file=sys.stderr)
        exit(1)
    else:
        with file:
            s = "".join(map(lambda line: line.strip(), file.readlines()))[2:]
            index = s.find(x)
            while index != -1:
                if counter < 5:
                    answers[counter] = index
                counter += 1
                index = s.find(x, index + 1)

    return counter, answers


class TestPiFinder(unittest.TestCase):

    def test_first(self):
        counter, positions = find_positions_in_pi("123", 'pi.txt')
        self.assertEqual(4185, counter)
        self.assertEqual([1923, 2937, 2975, 3891, 6547], positions)

    def test_second(self):
        counter, positions = find_positions_in_pi("1415", 'pi.txt')
        self.assertEqual(424, counter)
        self.assertEqual([0, 6954, 29135, 45233, 79686], positions)


if __name__ == '__main__':
    unittest.main()
