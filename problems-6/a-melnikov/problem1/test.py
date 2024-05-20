import unittest
from main import shuffle_text

class TestTextShuffling(unittest.TestCase):
    def test_shuffling(self) -> None:
        src = "abcdefg-abcdefg   abcdefg,.abcdefg"
        res = shuffle_text(src)
        self.assertEqual(src[0], res[0])
        self.assertEqual(src[6], res[6])
        self.assertEqual(src[7], res[7])
        self.assertEqual(src[8], res[8])
        self.assertEqual(src[14], res[14])
        self.assertEqual(src[15], res[15])
        self.assertEqual(src[16], res[16])
        self.assertEqual(src[17], res[17])
        self.assertEqual(src[18], res[18])
        self.assertEqual(src[24], res[24])
        self.assertEqual(src[25], res[25])
        self.assertEqual(src[26], res[26])
        self.assertEqual(src[27], res[27])
        self.assertEqual(src[33], res[33])
    
    def test_sorting(self) -> None:
        src = "aecbfdg-acdbfeg   abedfcg,.acfdebg"
        res = shuffle_text(src, True)
        self.assertEqual(res, "abcdefg-abcdefg   abcdefg,.abcdefg")

if __name__ == "__main__":
    unittest.main()
