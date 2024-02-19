class TenGreenBottles:

    _bottle: str = "green bottle"

    _numbers: dict[int, str] = {
        0: "no",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
    }

    def _form_noun(self, noun: str, amount: int) -> str:
        return noun if amount == 1 else noun + "s"

    def form_stanza(self, n: int) -> str:
        return (
            "%s %s hanging on the wall,\n"
            % (self._numbers[n].title(), self._form_noun(self._bottle, n))
            * 2
            + "And if %s %s should accidentally fall,\n"
            % (self._numbers[1], self._bottle)
            + "There’ll be %s %s hanging on the wall."
            % (self._numbers[n - 1], self._form_noun(self._bottle, n - 1))
        )


if __name__ == "__main__":
    for i in range(10, 0, -1):
        print(TenGreenBottles().form_stanza(i))
