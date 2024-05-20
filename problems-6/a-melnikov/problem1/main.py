import random
from enum import Enum


class State(Enum):
    TEXT = 1
    WORD = 2


def process_word(word: str, alphabetical_order: bool) -> str:
    res_word: str = ""
    if len(word) > 3:
        middle_word = list(word[1:-1])

        if alphabetical_order:
            middle_word.sort()
        else:
            random.shuffle(middle_word)

        res_word += word[0] + "".join(middle_word) + word[-1:]
    else:
        res_word += word
    return res_word


def shuffle_text(text: str, alphabetical_order: bool = False) -> str:
    res_text: str = ""
    state: State = State.TEXT
    first_char_idx: int = 0

    for i, c in enumerate(text):
        if state == State.TEXT:
            if c.isalpha():
                first_char_idx = i
                state = State.WORD
            else:
                res_text += c
        elif state == State.WORD:
            if not c.isalpha():
                res_text += process_word(text[first_char_idx:i], alphabetical_order) + c
                state = State.TEXT

    if state == State.WORD:
        res_text += process_word(text[first_char_idx:], alphabetical_order)
    return res_text
