

class CartesianProductIterator:

    def __init__(self, x, n, cyclic=False):
        self.x = x
        self.n = n
        self.cyclic = cyclic
        self.current_combination = [0] * n
        self.total_combinations = len(x) ** n
        self.current_index = 0

    def get_current_element(self):
        return tuple(self.x[i] for i in self.current_combination)

    def next_element(self):
        if self.current_index < self.total_combinations:
            self.current_index += 1
            for i in range(self.n - 1, -1, -1):
                if self.current_combination[i] < len(self.x) - 1:
                    self.current_combination[i] += 1
                    break
                elif i > 0:
                    self.current_combination[i] = 0
                elif self.cyclic:
                    self.current_combination = [0] * self.n
                else:
                    raise StopIteration("No more elements")
        else:
            raise StopIteration("No more elements")
