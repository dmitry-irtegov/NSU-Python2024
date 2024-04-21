import os.path
import sys
import time
import unittest


def readline_and_count(file):
    line = file.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line, len(line)


def find_positions_in_pi(x, file_path):
    counter = 0
    current_pos = 0
    answers = [0] * 5
    file = None
    try:
        if not os.access(file_path, os.R_OK):
            print("Can't read from file", file=sys.stderr)
            exit(1)
        if not os.path.isfile(file_path):
            print("File doesn't exist", file=sys.stderr)
            exit(1)
        file = open(file_path, 'r', encoding='utf-8')

        line, line_len = readline_and_count(file)
        to_check_first = []
        while line_len != 0:
            while len(to_check_first) > 0:
                to_check = to_check_first[0]
                if to_check[0] == line[:len(to_check[0])]:
                    if counter < 5:
                        answers[counter] = to_check[1]
                    counter += 1
                to_check_first = to_check_first[1:]

            index = line.find(x)

            while index != -1:
                last_in_line = index

                if counter < 5:
                    answers[counter] = current_pos + index
                counter += 1
                index = line.find(x, last_in_line + 1)

            for i in reversed(range(1, len(x))):
                if line[-i:] == x[:i]:
                    to_check_first.append([x[i:], current_pos + line_len - i])

            current_pos += line_len
            line, line_len = readline_and_count(file)
    finally:
        if file is not None:
            file.close()

    return counter, answers


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


def easier_solution(x, file_path):
    counter = 0
    answers = [0] * 5
    with open(file_path, "r") as file:
        s = "".join(map(lambda y: y.strip(), file.readlines()))
        index = s.find(x)
        while index != -1:
            if counter < 5:
                answers[counter] = index
            counter += 1
            index = s.find(x, index + 1)
    return counter, answers


class TestPiFinder(unittest.TestCase):
    def test_first_hard_algorithm(self):
        counter, positions = find_positions_in_pi("123", 'pi.txt')
        self.assertEqual(4185, counter)
        self.assertEqual([1923, 2937, 2975, 3891, 6547], positions)

    def test_second_hard_algorithm(self):
        counter, positions = find_positions_in_pi("1415", 'pi.txt')
        self.assertEqual(424, counter)
        self.assertEqual([0, 6954, 29135, 45233, 79686], positions)

    def test_first_easy_algorithm(self):
        counter, positions = easier_solution("123", 'pi.txt')
        self.assertEqual(4185, counter)
        self.assertEqual([1923, 2937, 2975, 3891, 6547], positions)

    def test_second_easy_algorithm(self):
        counter, positions = easier_solution("1415", 'pi.txt')
        self.assertEqual(424, counter)
        self.assertEqual([0, 6954, 29135, 45233, 79686], positions)

    def test_speed(self):
        start = time.perf_counter()
        _, _ = find_positions_in_pi("123", 'pi.txt')
        res1 = time.perf_counter() - start

        start = time.perf_counter()
        _, _ = easier_solution("123", 'pi.txt')
        res2 = time.perf_counter() - start
        self.assertTrue(res1 >= res2)


if __name__ == '__main__':
    unittest.main()
