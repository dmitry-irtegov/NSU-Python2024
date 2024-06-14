from util import parse_str, make_replacement_map, replace


class TestTranslate:
    def test_simple(self):
        assert tuple(parse_str('abc12 !! -')) == tuple('abc12 !! -')

    def test_hex(self):
        assert tuple(parse_str("\\x4B\\u040e")) == tuple("\x4b\u040E")

    def test_octal(self):
        assert tuple(parse_str("\\123\\45")) == tuple("\123\45")

    def test_escape(self):
        assert tuple(parse_str("\\0\\r\\n\\t\\\\\\b")) == tuple("\0\r\n\t\\\b")

    def test_line_term(self):
        assert tuple(parse_str('\n')) == ('\n',)

    def test_range(self):
        assert (list(parse_str("1-1a-zP-S")) ==
                ['1'] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['P', 'Q', 'R', 'S'])

    def test_many(self):
        s = 'd3s \\12\na-d\\u0333\\n!'
        assert tuple(parse_str(s)) == tuple('d3s \12\nabcd\u0333\n!')

    def test_replacement_simple(self):
        m = make_replacement_map('qg4! 0.-', '-3 11qwe')
        assert m == {'q': '-', 'g': '3', '4': ' ', '!': '1', ' ': '1', '0': 'q', '.': 'w', '-': 'e'}

    def test_replacement_override(self):
        m = make_replacement_map('121', 'abc')
        assert m == {'1': 'c', '2': 'b'}

    def test_replacement_no_trunc(self):
        m = make_replacement_map('abcdefg', '1234')
        assert m == {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '4', 'f': '4', 'g': '4'}

    def test_replacement_trunc(self):
        m = make_replacement_map('abcdefg', '1234', trunc=True)
        assert m == {'a': '1', 'b': '2', 'c': '3', 'd': '4'}

    def test_replacements_delete(self):
        m = make_replacement_map('abcd', '1234', delete='cat')
        assert m == {'a': '', 'b': '2', 'c': '', 'd': '4', 't': ''}

    def test_replace(self):
        m = {'a': '1', '2': 'b', 'z': ''}
        s = 'abcdefg uvwxyz 12345'
        assert replace(s, m) == '1bcdefg uvwxy 1b345'

    def test_integration1(self):
        s = 'abc\ndef'
        string1 = 'abcde\\n'
        string2 = '1-6'
        m = make_replacement_map(string1, string2)
        assert replace(s, m) == '123645f'

    def test_integration2(self):
        s = 'qwertasdfghzxcvb 012345!@#,./()-='
        string1 = 'qg4! 0.-'
        string2 = '-3 a-e'
        m = make_replacement_map(string1, string2)
        assert replace(s, m) == '-wertasdf3hzxcvbbc123 5a@#,d/()e='

    def test_integration_delete(self):
        s = "AaBbCcDdEeFf...UuVvWvXxYyZz"
        string1 = 'a-j'
        string2 = '0-9'
        delete = 'd-w'
        m = make_replacement_map(string1, string2, delete=delete)
        assert replace(s, m) == 'A0B1C2DEF...UVWXxYyZz'
