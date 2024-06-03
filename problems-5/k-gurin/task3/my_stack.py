class MyStack:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        elif not isinstance(elements, list):
            raise TypeError("elements must be a list")
        else:
            self.elements = elements.copy()

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def __len__(self):
        return len(self.elements)
