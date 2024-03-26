from typing import List, Any
from copy import deepcopy, copy


class Table:
    rows: int
    columns: int
    content: List[List[Any]]

    def __init__(self, rows: int, columns: int, content=None) -> None:

        if rows < 1 or columns < 1:
            raise ValueError('rows and columns must be greater than 0')

        if content is not None:
            new_rows = len(content)
            if new_rows != rows:
                raise ValueError('rows of content and in passed variable must be the same')
            if not all(map(lambda row: len(row) == columns, content)):
                raise ValueError('length of each row of content must be the same')

            self.content = deepcopy(content)
        else:
            self.content = [[None] * columns for _ in range(rows)]

        self.rows = rows
        self.columns = columns

    def get_by_row_and_column(self, row, column) -> Any:
        if row < 0 or row >= self.rows:
            raise ValueError('row must be between -1 and rows')
        if column < 0 or column >= self.columns:
            raise ValueError("column must be between -1 and columns")

        return self.content[row][column]

    def get_row(self, index: int) -> List[Any]:
        if index < 0 or index >= self.rows:
            raise ValueError('index must be between -1 and rows')

        return self.content[index]

    def tail(self, number_of_rows: int) -> 'Table':
        if number_of_rows < 1 or number_of_rows > self.rows:
            raise ValueError('number_of_rows must be between 0 and rows')

        return Table(number_of_rows, self.columns, deepcopy(self.content[-number_of_rows:]))

    def head(self, number_of_rows: int) -> 'Table':
        if number_of_rows < 1 or number_of_rows > self.rows:
            raise ValueError('number_of_rows must be between 0 and rows')

        return Table(number_of_rows, self.columns, deepcopy(self.content[:number_of_rows]))

    def merge_rows(self, another_table: 'Table') -> None:
        if another_table.columns != self.columns:
            raise ValueError('another_table must have the same number of columns')

        self.content.extend(deepcopy(another_table.content))
        self.rows += another_table.rows

    def merge_columns(self, another_table: 'Table') -> None:
        if another_table.rows != self.rows:
            raise ValueError('another_table must have the same number of rows')

        for index, row in enumerate(another_table.content):
            self.content[index].extend(copy(row))

        self.columns += another_table.columns

    def create_table_with_rows(self, indices: List[int]) -> 'Table':
        if not all(map(lambda index: 0 <= index < self.rows, indices)):
            raise ValueError('indices must be between 0 and rows')

        new_content = []
        for index in indices:
            new_content.append(copy(self.get_row(index)))

        return Table(len(indices), self.columns, new_content)

    def __str__(self):
        return (f'Rows: {self.rows}\nColumns: {self.columns} \n' +
                f'{'\n'.join(map(lambda row: str(row), self.content))}\n')


if __name__ == '__main__':
    table_1 = Table(2, 3)
    table_2 = Table(2, 3, [[1, 2, 3], [4, 5, 6]])
    table_1_1 = deepcopy(table_1)

    table_1.merge_rows(table_2)
    print(table_1)

    table_2.merge_columns(table_1_1)
    print(table_2)

    print(table_2.head(2))

    print(table_2.tail(2))

    print(table_2.get_by_row_and_column(1, 1))
