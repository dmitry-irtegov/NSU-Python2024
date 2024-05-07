import unittest

BLOCK_SIZE = 10000


def find_positions_in_block(block, positions, substring, lower_bound):
    index = block.find(substring)
    while index != -1:
        positions.append(index + lower_bound)
        index = block.find(substring, index + 1)


def find_positions_in_pi(substring, file_path):
    positions = []
    offset = len(substring) - 1

    try:
        file = open(file_path, "r")
    except OSError as e:
        e.strerror = f"Cannot open file '{file_path}': " + e.strerror
        raise e
    except BaseException as e:
        e.args = (f"Cannot open file '{file_path}': ", *e.args)
        raise e
    with file:
        try:
            block = ""
            lower_bound = 0
            for line in file:
                block += line.strip()
                if len(block) >= BLOCK_SIZE:
                    find_positions_in_block(block, positions, substring, lower_bound)
                    lower_bound += len(block) - offset
                    block = block[-offset:]
            find_positions_in_block(block, positions, substring, lower_bound)
        except OSError as e:
            e.strerror = f"Trying read from file: '{file_path}', but: " + e.strerror
            raise e
        except BaseException as e:
            e.args = (f"Trying read from file: '{file_path}', but: ", *e.args)

    return positions


class TestPiFinder(unittest.TestCase):

    def test_first(self):
        positions = find_positions_in_pi("123", 'pi.txt')
        self.assertEqual(4185, len(positions))
        self.assertEqual([1923, 2937, 2975, 3891, 6547], positions[:5])

    def test_second(self):
        positions = find_positions_in_pi("1415", 'pi.txt')
        self.assertEqual(424, len(positions))
        self.assertEqual([0, 6954, 29135, 45233, 79686], positions[:5])

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            find_positions_in_pi("123", "123")
    

if __name__ == '__main__':
    unittest.main()
