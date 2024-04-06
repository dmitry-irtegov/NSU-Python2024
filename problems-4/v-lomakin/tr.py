# -*- coding: utf-8 -*-
def tr(string, replace_from, replace_to, delete_chars=None):
    if len(replace_from) != len(replace_to):
        raise ValueError('Строки замены и заменяемые строки должны быть одинаковой длины')
    if len(replace_from) != len(set(replace_from)):
        raise ValueError('Заменяемые символы не должны повторяться')
    
    def translate_char(c):
        if delete_chars and c in delete_chars:
            return None
        if c in replace_from:
            index = replace_from.index(c)
            return replace_to[index]
        else:
            return c

    res = ""
    for i in string:
        ch = translate_char(i)
        if ch is not None :
            res += ch
    return res
