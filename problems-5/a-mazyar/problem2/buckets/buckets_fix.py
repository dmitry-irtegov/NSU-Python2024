class Buckets(object):
    def __init__(self, length, default: list):
        self.default = default.copy() # fix default persists
        self.buckets = [self.default.copy() for _ in range(length)] # fix shared adds
 
    def add(self, index, element):
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = self.default
