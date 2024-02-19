import unittest

def trim_sequence(seq, a, b):
    trimmed_seq = [0]*len(seq)
    for i in range(len(seq)):
        if seq[i] < a:
            trimmed_seq[i] = a
        elif seq[i] > b:
            trimmed_seq[i] = b
        else:
            trimmed_seq[i] = seq[i]
    return trimmed_seq

class TestTrimSequence(unittest.TestCase):
    def test_trim_sequence(self):
        sequence = [1, 5, 10, 15, 20, 25]
        a = 5
        b = 20
        expected_trimmed_sequence = [5, 5, 10, 15, 20, 20]
        self.assertEqual(trim_sequence(sequence, a, b), expected_trimmed_sequence)

    def test_empty(self):
        sequence = []
        a = 5
        b = 20
        expected_trimmed_sequence = []
        self.assertEqual(trim_sequence(sequence, a, b), expected_trimmed_sequence)

    def test_no_trim_needed(self):
        sequence = [10, 15, 20]
        a = 5
        b = 25
        expected_trimmed_sequence = [10, 15, 20]
        self.assertEqual(trim_sequence(sequence, a, b), expected_trimmed_sequence)

    def test_all_trimmed(self):
        sequence = [1, 2, 3]
        a = 5
        b = 10
        expected_trimmed_sequence = [5, 5, 5]
        self.assertEqual(trim_sequence(sequence, a, b), expected_trimmed_sequence)

if __name__ == '__main__':
    unittest.main()
