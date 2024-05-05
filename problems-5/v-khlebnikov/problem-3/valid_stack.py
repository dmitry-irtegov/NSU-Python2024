from copy import deepcopy


class ValidStack(object):
    def __init__(self, elements=None):
        if elements is None:
            self.__elements = []
        else:
            self.__elements = deepcopy(elements)

    def push(self, el):
        self.__elements.append(el)

    def pop(self):
        try:
            return self.__elements.pop()
        except IndexError:
            raise IndexError("Can't pop from empty stack")

    def __len__(self):
        return len(self.__elements)
    