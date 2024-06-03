from copy import deepcopy


class MyStack:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = deepcopy(elements)

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        if len(self.elements) == 0:
            raise IndexError
        else:
            return self.elements.pop()

    def __len__(self):
        return len(self.elements)