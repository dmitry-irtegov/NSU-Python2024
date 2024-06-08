"""
Provides a Vector object.
"""

import math
from typing import overload, Sequence, Self, SupportsFloat, Iterable


class Vector(Sequence):
    """
    Class representing a coordinate vector.

    This object contains N floating point numbers that represent the coordinates.
    The size is set at initialization and cannot be changed.

    Parameters
    ----------
    arg : int or Sequence[SupportsFloat]
        If arg is int, create vector of x zeroes.
        If arg is Sequence[SupportsFloat], create vector from contents of x.
    """
    _value: list[float]

    @overload
    def __init__(self, size: int):
        """
        Create a vector of zeroes.

        Parameters
        ----------
        size : int
            Number of coordinates in the vector.
        """
        ...

    @overload
    def __init__(self, value: Iterable[SupportsFloat]):
        """
        Create a vector of given elements.

        Parameters
        ----------
        value : Sequence[SupportsFloat]
            Elements that will be the coordinates of the vector.
        """
        ...

    def __init__(self, arg):
        """
        Create a vector. This constructor is overloaded.

        Parameters
        ----------
        arg : int or Sequence[SupportsFloat]
            If arg is int, create vector of arg zeroes.
            If arg is Sequence[SupportsFloat], create vector from contents of arg.
        """
        if isinstance(arg, int):
            self._value = [0] * arg
        elif isinstance(arg, Sequence):
            self._value = [float(i) for i in arg]
        else:
            raise TypeError(f'constructor argument must be an integer or a sequence, not \'{type(arg)}\'')

    @overload
    def __getitem__(self, index: int) -> float:
        """
        Get ith element of the vector.

        Parameters
        ----------
        index : int
            Index of the coordinate to be returned.

        Returns
        -------
        float
            The ith coordinate of the vector.
        """
        ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[float]:
        """
        Get range of elements of the vector.

        Parameters
        ----------
        index : slice
            Range of the coordinate to be returned.

        Returns
        -------
        float
            The ith coordinate of the vector.
        """
        ...

    def __getitem__(self, index: int | slice) -> float | Sequence[float]:
        """
        Get one or multiple elements of the vector.

        Parameters
        ----------
        index : int or slice
            Index of the coordinate to be returned.

        Returns
        -------
        float or Sequence[float]
            One or multiple coordinates of the vector and index.
        """
        return self._value[index]

    @overload
    def __setitem__(self, index: int, value: float) -> None:
        """
        Set one or multiple elements of the vector.

        Parameters
        ----------
        index : int
            Index of the coordinate to set.
        value : float
            Value to set at this coordinate.
        """
        ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[float]) -> None:
        """
        Set one or multiple elements of the vector.

        Parameters
        ----------
        index : int
            Index of the coordinate to set.
        value : float
            Value to set at this coordinate.
        """
        ...

    def __setitem__(self, index, value) -> None:
        """
        Set one or multiple elements of the vector.

        Parameters
        ----------
        index : int or slice
            Range of the coordinates to set.
        value : float | Iterable[float]
            Values to set at these coordinates.
        """
        self._value[index] = value

    def __len__(self) -> int:
        """
        Get number of coordinates in the vector.

        Returns
        -------
        int
            Number of coordinates in the vector.
        """
        return len(self._value)

    def clone(self) -> Self:
        """
        Clone the vector so that the copy can be mutated without changing the original.

        Returns
        -------
        Vector
            A clone of this vector.
        """
        return self.__class__(self._value)

    def __repr__(self) -> str:
        """
        Return a string containing a printable representation of the vector that can be used in eval().

        Returns
        -------
        str
            Representation of the vector.
        """
        return f'Vector({repr(self._value)})'

    def __str__(self) -> str:
        """
        Return a string containing the nicely printable string representation of the vector.

        Returns
        -------
        str
            Representation of the vector.
        """
        return f'Vector[{', '.join(map(str, self._value))}]'

    def __iadd__(self, other: Self) -> Self:
        """
        Increase vector by another vector.

        Parameters
        ----------
        other : Vector
            Another vector to add.

        Returns
        -------
        Vector
            Reference to self.
        """
        for i in range(len(self._value)):
            self._value[i] += other._value[i]
        return self

    def __add__(self, other: Self) -> Self:
        """
        Get the sum of two vectors.

        Parameters
        ----------
        other : Vector
            Another vector to add.

        Returns
        -------
        Vector
            A new vector containing sum of two vectors.
        """
        ret = self.clone()
        ret += other
        return ret

    def __isub__(self, other: Self) -> Self:
        """
        Decrease vector by another vector.

        Parameters
        ----------
        other : Vector
            Another vector to subtract.

        Returns
        -------
        Vector
            Reference to self.
        """
        for i in range(len(self._value)):
            self._value[i] -= other._value[i]
        return self

    def __sub__(self, other: Self) -> Self:
        """
        Get the difference of two vectors.

        Parameters
        ----------
        other : Vector
            Another vector to subtract.

        Returns
        -------
        Vector
            A new vector containing difference of two vectors.
        """
        ret = self.clone()
        ret -= other
        return ret

    def __imul__(self, scalar: SupportsFloat) -> Self:
        """
        Multiply the vector by a scalar.

        Parameters
        ----------
        scalar : float
            Scalar value to multiply the vector by.

        Returns
        -------
        Vector
            Reference to self.
        """
        scalar = float(scalar)
        for i in range(len(self._value)):
            self._value[i] *= scalar
        return self

    def __mul__(self, scalar: SupportsFloat) -> Self:
        """
        Get the vector multiplied by a scalar.

        Parameters
        ----------
        scalar : float
            Scalar value to multiply the vector by.

        Returns
        -------
        Vector
            A new vector containing this vector multiplied by a scalar.
        """
        ret = self.clone()
        ret *= scalar
        return ret

    def __neg__(self) -> Self:
        """
        Get the negative of the vector.

        Returns
        -------
        Vector
            A new negated vector.
        """
        return self * -1

    def __eq__(self, other: object) -> bool:
        """
        Compare two vectors.

        Parameters
        ----------
        other : Vector
            Another vector to compare.

        Returns
        -------
        bool
            True if the vectors are equal, False otherwise.
        """
        if not isinstance(other, Vector):
            return False
        for i in zip(self._value, other._value):
            if i[0] != i[1]:
                return False
        return True

    def dot(self, other: Self) -> float:
        """
        Compute the dot product of two vectors.

        Parameters
        ----------
        other : Vector
            Another vector to compute dot product.

        Returns
        -------
        float
            The dot product of the vectors.
        """
        return sum(map(lambda t: t[0] * t[1], zip(self._value, other._value)))

    def __abs__(self) -> float:
        """
        Compute the Euclidean norm of the vector.

        Returns
        -------
        float
            The Euclidean norm of the vector.
        """
        return math.sqrt(self.dot(self))
