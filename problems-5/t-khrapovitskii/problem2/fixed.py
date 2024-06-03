from collections.abc import Collection


class FixedBuckets:
    def __init__(self, length: int, default: Collection):
        self.default = tuple(default)
        self.buckets = [set(self.default) for _ in range(length)]

    def add(self, index: int, element):
        self.buckets[index].add(element)

    def find(self, index: int, element) -> bool:
        return element in self.buckets[index]

    def clear(self, index: int):
        self.buckets[index] = set(self.default)
