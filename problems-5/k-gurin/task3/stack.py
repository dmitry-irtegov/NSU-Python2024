class Stack(object):
    def __init__(self, elements=[]):
        self.elements = elements

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def __len__(self):
        return len(self.elements)