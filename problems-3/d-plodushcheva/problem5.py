class Table:
    """
    Класс, представляющий таблицу данных.

    Этот класс позволяет выполнять различные операции с данными в таблице,
    такие как отображение первых или последних строк, выбор конкретных строк
    или столбцов, а также объединение таблиц по строкам или столбцам.

    Attributes
    ----------
    data : list
        Двумерный список, представляющий данные в таблице.
        Каждый элемент внешнего списка представляет строку в таблице,
        а элементы внутренних списков - значения в ячейках соответствующей строки.
    """

    def __init__(self, data):
        """
        Создание таблицы из входных данных.

        Parameters
        ----------
        data : []
            Двумерный список, представляющий данные в таблице
        """
        self.data = data

    def head(self, n):
        """
        Отсекает первые n строк.

        Parameters
        ----------
        n : int
            Количество нужных строк

        Returns
        -------
        Table
            Таблица из первых n строк
        """
        return Table(self.data[:n])

    def tail(self, n):
        """
        Отсекает последние n строк.

        Parameters
        ----------
        n : int
            Количество нужных строк

        Returns
        -------
        Table
            Таблица из последних n строк
        """
        return Table(self.data[-n:])

    def select_rows(self, indices):
        """
        Берет строки по указанным индексам.

        Parameters
        ----------
        indices : [int]
            Массив индексов нужных строк

        Returns
        -------
        Table
            Таблица из выбранных строк
        """
        return Table([self.data[i] for i in indices])

    def select_columns(self, indices):
        """
        Берет столбцы по указанным индексам.

        Parameters
        ----------
        indices : [int]
            Массив индексов нужных столбцов

        Returns
        -------
        Table
            Таблица из выбранных столбцов
        """
        return Table([[row[i] for i in indices] for row in self.data])

    def concat_rows(self, other_table):
        """
        Соединяет две таблицы по строкам.

        Parameters
        ----------
        other_table : Table
            Присоединяемая таблица - строки

        Returns
        -------
        Table
            Результат объединения двух таблиц

        Notes
        -----
        Число строк в обеих таблицах должно быть одинаковым
        """
        return Table(self.data + other_table.data)

    def concat_columns(self, other_table):
        """
        Соединяет две таблицы по столбцам.

        Parameters
        ----------
        other_table : Table
            Присоединяемая таблица - столбцы

        Returns
        -------
        Table
            Результат объединения двух таблиц
        """
        return Table([row + other_row for row, other_row in zip(self.data, other_table.data)])

    def __eq__(self, other):
        """
        Проверяет на равенство.

        Parameters
        ----------
        other : Table
            Таблица, с которой идет сравнение

        Returns
        -------
        bool
            Результат проверки на равенство
        """
        if isinstance(other, Table):
            return self.data == other.data
        return False
