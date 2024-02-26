import unittest


def find_substring(num):
    string_occurrences = []
    found_occurrence = 0

    pi = open("pi.txt").read().replace('\n', '')[2:]

    while (found_occurrence := pi.find(num, found_occurrence)) != -1:
        string_occurrences.append(found_occurrence)
        found_occurrence += 1

    return len(string_occurrences), string_occurrences[:5]


class TestFindSubstring(unittest.TestCase):

    def test_first_example(self):
        excepted = (4185, [1923, 2937, 2975, 3891, 6547])
        self.assertTupleEqual(excepted, find_substring("123"))

    def test_second_example(self):
        excepted = (424, [0, 6954, 29135, 45233, 79686])
        self.assertTupleEqual(excepted, find_substring("1415"))

    def test_single_number(self):
        excepted = (419139, [0, 2, 36, 39, 48])
        self.assertTupleEqual(excepted, find_substring("1"))


if __name__ == "__main__":
    unittest.main()
