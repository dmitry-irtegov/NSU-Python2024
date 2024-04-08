import unittest


def find_substring(num):
    occurrences = []
    last_sliced_index = 0
    chunks = ""
    with open("pi.txt") as f:
        while True:
            chunk = f.read(10000)
            if not chunk:
                break

            chunk = chunk.replace('\n', '')

            chunks += chunk

            occurrence_index = chunks.find(num)
            while occurrence_index != -1:
                occurrences.append(last_sliced_index + occurrence_index)
                occurrence_index += 1
                last_sliced_index += occurrence_index
                chunks = chunks[occurrence_index:]
                occurrence_index = chunks.find(num)

    return len(occurrences), occurrences[:5]


class TestFindSubstring(unittest.TestCase):

    def test_digit(self):
        self.assertTupleEqual((419907, [14, 30, 40, 48, 57]), find_substring("7"))

    def test_small_num(self):
        self.assertTupleEqual((4185, [1925, 2939, 2977, 3893, 6549]), find_substring("123"))

    def test_big_num(self):
        self.assertTupleEqual((1, [2587993]), find_substring("9925449022087269459849405"))

    def test_large_num(self):
        self.assertTupleEqual(
            (1, [3509922]),
            find_substring(
                "1298089764749344925275601751397259626844842134839054624385860528916070194755434157027205684181170287"))


if __name__ == "__main__":
    unittest.main()
