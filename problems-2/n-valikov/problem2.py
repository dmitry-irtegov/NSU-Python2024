import unittest


def solve(data: str) -> list[tuple[str, str]]:
    result = dict()
    for line in data.splitlines():
        lexems = line.replace(',', '').split()
        for word in lexems[2:]:
            result[word] = result[word] + [lexems[0]] \
                if word in result.keys() else [lexems[0]]
    result = dict(sorted(result.items()))
    return [(key, ", ".join(result[key])) for key in result]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        data = """
            apple - malum, pomum, popula
            fruit - baca, bacca, popum
            punishment - malum, multa
            """
        self.assertEqual(solve(data), [('baca', 'fruit'), ('bacca', 'fruit'),
                                       ('malum', 'apple, punishment'), ('multa', 'punishment'),
                                       ('pomum', 'apple'), ('popula', 'apple'),
                                       ('popum', 'fruit')])


if __name__ == '__main__':
    unittest.main()
