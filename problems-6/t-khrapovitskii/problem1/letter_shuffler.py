import typing
from collections.abc import Callable


class LetterShuffler:
    def __init__(self, shuffle_func: Callable[[list[str]], None], output: typing.TextIO):
        self.func = shuffle_func
        self.output = output
        self.first: str | None = None
        self.middle: list[str] = []

    def give_char(self, char: str):
        if len(char) != 1:
            raise ValueError('Letter must be a single character')
        if char.isalpha():
            if self.first:
                self.middle.append(char)
            else:
                self.first = char
        else:
            if self.first:
                self._shuffle_word()
            self.output.write(char)

    def finish(self):
        if self.first:
            self._shuffle_word()

    def _shuffle_word(self):
        self.output.write(self.first)
        self.first = None
        if self.middle:
            last = self.middle.pop()
            self.func(self.middle)
            for i in self.middle:
                self.output.write(i)
            self.output.write(last)
            self.middle.clear()
