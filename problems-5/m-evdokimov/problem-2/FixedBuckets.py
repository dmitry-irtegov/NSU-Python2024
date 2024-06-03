class FixedBuckets(object):
    def __init__(self, length, default):
        try:
            self.default = list(default)
        except Exception as e:
            raise type(e)("argument 'default' in Fixed_Buckets(length, default) must be a sequence") from e
        if length < 1:
            raise ValueError("the number of baskets cannot be less than one")
        self.buckets = [self.default.copy() for i in range(length)]

    def add(self, index, element):
        self.buckets[index].append(element)

    def find(self, index, element):
        return element in self.buckets[index]

    def clear(self, index):
        self.buckets[index] = self.default.copy()