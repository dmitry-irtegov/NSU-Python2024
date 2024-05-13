import sys
import unittest
import io

from pathlib import Path
from unittest.mock import patch

class MalformedDictionaryException(Exception):
    def __init__(self, line: str, *args: object) -> None:
        super().__init__(*args)
        self.malformed_line = line

def parse_line(line: str) -> tuple[str, list[str]]:
    line = line.strip().removesuffix('\n')
    parts = line.split(' - ')

    if len(parts) != 2:
        raise MalformedDictionaryException(line)

    key = parts[0]
    translations = parts[1].split(', ')

    if any([ not x.isalpha() for x in translations ]):
        raise MalformedDictionaryException(line)

    return key, translations

def parse_dict(path: Path) -> dict[str, list[str]]:
    lines = []

    with open(path) as file:
        lines = file.readlines()

    source_dict = {}

    for line in lines:
        try:
            key, translations = parse_line(line)
            source_dict[key] = translations
        except MalformedDictionaryException as e:
            print(f'Malformed dictionary entry, skipping; Problematic line: {e.malformed_line}', file=sys.stderr)

    return source_dict

def write_dict(path: Path, new_dict: dict[str, list[str]]):
    with open(path, 'w') as file:
        for key, translations in sorted(new_dict.items()):
            file.write("{} - {}\n".format(key, ", ".join(sorted(translations)))) 

def reverse_dict(source_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    new_dict: dict[str, list[str]] = {}

    for key, translations in source_dict.items():
        for translation in translations:
            if translation not in new_dict:
                new_dict[translation] = [key]
            else:
                new_dict[translation].append(key)

    return new_dict

def translate_file(in_file: Path, out_file: Path):
    try:
        write_dict(
            out_file,
            reverse_dict(
                parse_dict(in_file)
            )
        )
    except FileNotFoundError as e:
        print(f'Input file was not found: {e.filename}', file=sys.stderr)

class TestTranslator(unittest.TestCase):

    source_dict = {'apple': ['malum', 'pomum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa']}
    reversed_dict = {'baca': ['fruit'], 'bacca': ['fruit'], 'malum': ['apple', 'punishment'], 'multa': ['punishment'], 'pomum': ['apple'], 'popula': ['apple'], 'popum': ['fruit']}

    def test_parse_dict(self):
        parsed_dict = parse_dict(Path(__file__).parent / 'dict.txt')

        self.assertEqual(parsed_dict, TestTranslator.source_dict)

    def test_reverse_dict(self):
        reversed_dict = reverse_dict(TestTranslator.source_dict)

        self.assertEqual(reversed_dict, TestTranslator.reversed_dict)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_parse_malformed(self, mock_stderr):
        parsed_dict = parse_dict(Path(__file__).parent / 'malformed.txt')

        self.assertEqual(parsed_dict, { 'punishment': ['malum'] })
        self.assertTrue(mock_stderr.getvalue() != '')

    def test_translate_file(self):
        translate_file(
            Path(Path(__file__).parent / 'dict.txt'), 
            Path(Path(__file__).parent / 'new_dict.txt')
        )

        parsed_dict = parse_dict(Path(Path(__file__).parent / 'new_dict.txt'))

        self.assertEqual(parsed_dict, TestTranslator.reversed_dict)

    @patch('sys.stderr', new_callable=io.StringIO)
    def test_wrong_filename(self, mock_stderr):
        translate_file(
                    Path(Path(__file__).parent / 'dinhghjct.txt'), 
                    Path(Path(__file__).parent / 'new_dict.txt')
                )
        
        self.assertTrue(mock_stderr.getvalue().startswith('Input file was not found'))

if __name__ == '__main__':
    unittest.main()
