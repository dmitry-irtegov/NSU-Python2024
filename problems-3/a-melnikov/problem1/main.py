from typing import Self, TypeVar, Generic

T = TypeVar("T")


class Table(Generic[T]):

    rows: int
    columns: int
    table: list[list[T | None]]

    def __init__(self, rows: int, columns: int, table: list[list[T | None]] | None = None):
        self.rows = rows
        self.columns = columns
        self.table: list[list[T | None]] = [[None] * columns for _ in range(rows)]
        if table is not None:
            for i in range(rows):
                for j in range(columns):
                    self.table[i][j] = table[i][j]

    def tail(self, count: int) -> Self:
        assert count > 0 and count < self.rows
        return self.select_rows(*[i for i in range(self.rows - count, self.rows)])

    def head(self, count: int) -> Self:
        assert count > 0 and count < self.rows
        return self.select_rows(*[i for i in range(count)])

    def select_rows(self, *row_indices: int) -> Self:
        rows: int = len(row_indices)
        table: list[list[T | None]] = [[None] * self.columns for _ in row_indices]
        for i, row in enumerate(row_indices):
            for j in range(self.columns):
                table[i][j] = self.table[row][j]
        return Table(rows, self.columns, table)

    def select_columns(self, *column_indices: int) -> Self:
        columns: int = len(column_indices)
        table: list[list[T | None]] = [[None] * len(column_indices) for _ in range(self.rows)]
        for i in range(self.rows):
            for j, col in enumerate(column_indices):
                table[i][j] = self.table[i][col]
        return Table(self.rows, columns, table)

    def join_rows(self, table: Self) -> Self:
        if table.columns != self.columns:
            raise IndexError("Count of columns in two tables do not match")
        columns: int = self.columns
        rows: int = self.rows + table.rows
        res_table: list[list[T | None]] = [[None] * columns for _ in range(rows)]

        for j in range(columns):
            for i in range(self.rows):
                res_table[i][j] = self.table[i][j]

            for i in range(table.rows):
                res_table[self.rows + i][j] = table.table[i][j]

        return Table(rows, columns, res_table)

    def join_columns(self, table: Self) -> Self:
        if table.rows != self.rows:
            raise IndexError("Count of rows in two tables do not match")
        columns: int = self.columns + table.columns
        rows: int = self.rows
        res_table: list[list[T | None]] = [[None] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(self.columns):
                res_table[i][j] = self.table[i][j]

            for j in range(table.columns):
                res_table[i][self.columns + j] = table.table[i][j]

        return Table(rows, columns, res_table)
