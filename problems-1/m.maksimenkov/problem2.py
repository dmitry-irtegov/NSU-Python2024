import unittest


def seq_cut(nums, a, b):
    for idx, num in enumerate(nums):
        if num < a:
            nums[idx] = a
        elif num > b:
            nums[idx] = b
    return nums


class TestCumulativeSums(unittest.TestCase):

    def test(self):
        self.assertEqual(seq_cut([1, 2, 3], 2, 2), [2, 2, 2])
        self.assertEqual(seq_cut([-5, 1334, 3221, 543], 1600, 3000), [1600, 1600, 3000, 1600])


if '__main__' == __name__:
    unittest.main()
