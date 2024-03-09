class Table:
    def __init__(self, data):
        self.data = data

    def head(self, n):
        return Table(self.data[:n])

    def tail(self, n):
        return Table(self.data[-n:])

    def select_rows(self, indices):
        return Table([self.data[i] for i in indices])

    def select_columns(self, indices):
        return Table([[row[i] for i in indices] for row in self.data])

    def concat_rows(self, other_table):
        return Table(self.data + other_table.data)

    def concat_columns(self, other_table):
        return Table([row + other_row for row, other_row in zip(self.data, other_table.data)])

    def __eq__(self, other):
        if isinstance(other, Table):
            return self.data == other.data
        return False
