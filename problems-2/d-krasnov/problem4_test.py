import unittest

from problem4 import find_sequence

class TestFindSequence(unittest.TestCase):
    def test_find_sequence_123(self):
        pi_file = 'pi.txt'
        sequence = '123'
        expected_result = [1923, 2937, 2975, 3891, 6547]
        self.assertEqual(find_sequence(sequence, pi_file)[:5], expected_result)

    def test_find_sequence_999(self):
        pi_file = 'pi.txt'
        sequence = '999'
        expected_result = [761, 762, 763, 764, 2948]
        self.assertEqual(find_sequence(sequence, pi_file)[:5], expected_result)

if __name__ == '__main__':
    unittest.main()

