import unittest

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


class TestFindSequence(unittest.TestCase):

    def test_first_example(self):
        expected_count = 4185
        actual_count = len(find_sequence("123"))
        self.assertEqual(expected_count, actual_count)

    def test_second_example(self):
        expected_count = 424
        actual_count = len(find_sequence("1415"))
        self.assertEqual(expected_count, actual_count)

    def test_third_example(self):
        expected_count = 475
        actual_count = len(find_sequence("9999"))
        self.assertEqual(expected_count, actual_count)

    def test_fourth_example(self):
        expected_count = 57
        actual_count = len(find_sequence("99999"))
        self.assertEqual(expected_count, actual_count)

    def test_fifth_example(self):
        expected_count = 41696
        actual_count = len(find_sequence("22"))
        self.assertEqual(expected_count, actual_count)


if __name__ == "__main__":
    unittest.main()
