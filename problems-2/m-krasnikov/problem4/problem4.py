import os
import time
import unittest

import psutil


def find_substring_chunks(num):
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


def find_substring_lines(num):
    occurrences = []
    occurrence_index = 0
    pi = ""

    with open("pi.txt") as f:
        for line in f.readlines():
            pi += line.replace('\n', '')

        occurrence_index = pi.find(num, occurrence_index)
        while occurrence_index != -1:
            occurrences.append(occurrence_index)
            occurrence_index += 1
            occurrence_index = pi.find(num, occurrence_index)

        return len(occurrences), occurrences[:5]


class TestFindSubstring(unittest.TestCase):

    def test_digit_chunks(self):
        time_start = time.process_time()
        self.assertTupleEqual((419907, [14, 30, 40, 48, 57]), find_substring_chunks("7"))
        print(
            f"test_digit_chunks: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_digit_lines(self):
        time_start = time.process_time()
        self.assertTupleEqual((419907, [14, 30, 40, 48, 57]), find_substring_lines("7"))
        print(
            f"test_digit_lines: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_small_num_chunks(self):
        time_start = time.process_time()
        self.assertTupleEqual((4185, [1925, 2939, 2977, 3893, 6549]), find_substring_chunks("123"))
        print(
            f"test_small_num_chunks: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_small_num_lines(self):
        time_start = time.process_time()
        self.assertTupleEqual((4185, [1925, 2939, 2977, 3893, 6549]), find_substring_lines("123"))
        print(
            f"test_small_num_lines: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_big_num_chunks(self):
        time_start = time.process_time()
        self.assertTupleEqual((1, [2587993]), find_substring_chunks("9925449022087269459849405"))
        print(
            f"test_big_num_chunks: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_big_num_lines(self):
        time_start = time.process_time()
        self.assertTupleEqual((1, [2587993]), find_substring_lines("9925449022087269459849405"))
        print(
            f"test_big_num_lines: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_large_num_chunks(self):
        time_start = time.process_time()
        self.assertTupleEqual(
            (1, [3509922]),
            find_substring_chunks(
                "1298089764749344925275601751397259626844842134839054624385860528916070194755434157027205684181170287"))
        print(
            f"test_large_num_chunks: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")

    def test_large_num_lines(self):
        time_start = time.process_time()
        self.assertTupleEqual(
            (1, [3509922]),
            find_substring_lines(
                "1298089764749344925275601751397259626844842134839054624385860528916070194755434157027205684181170287"))
        print(
            f"test_large_num_lines: time - {time.process_time() - time_start}, "
            f"memory - {psutil.Process(os.getpid()).memory_info().peak_wset}")


if __name__ == "__main__":
    unittest.main()
