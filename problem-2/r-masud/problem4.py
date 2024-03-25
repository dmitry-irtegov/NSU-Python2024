import unittest

def find_substring(num):
    string_occurrences = []
    found_occurrence = 0

    with open("pi.txt", "r") as f:
        pi = f.read().replace('\n', '')[2:]


    while found_occurrence < len(pi):
        found_occurrence = pi.find(num, found_occurrence)
        if found_occurrence == -1:
            break
        string_occurrences.append(found_occurrence)
        found_occurrence += 1

    return len(string_occurrences), string_occurrences[:5]

class TestFindSubstring(unittest.TestCase):

    def test_first_example_sequence(self):
        expected = (4185, [1923, 2937, 2975, 3891, 6547])
        self.assertTupleEqual(expected, find_substring("123"))

    def test_second_example_sequence(self):
        expected = (424, [0, 6954, 29135, 45233, 79686])
        self.assertTupleEqual(expected, find_substring("1415"))

    def test_single_digit(self):
        expected = (420192, [4, 11, 13, 29, 37])
        self.assertTupleEqual(expected, find_substring("9"))

    def test_sequence_at_end_of_pi(self):
        expected = (475, [761, 762, 763, 17987, 19436])
        self.assertTupleEqual(expected, find_substring("9999"))


if __name__ == "__main__":
    unittest.main()
