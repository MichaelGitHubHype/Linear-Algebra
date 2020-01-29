from __future__ import annotations
from typing import List


class MatrixShapeError(Exception):
    def __str__(self) -> str:
        return "Oops, it seems like your matrix did not match it's shape."


class MatrixDimensionError(Exception):
    def __str__(self) -> str:
        return "Hello, these matrix dimensions do not match."


class Matrix:
    """A Linear Algebra Matrix"""

    _matrix: List[List[int]]
    rows: int
    columns: int

    def __init__(self, m: int, n: int, mtrix=None) -> None:
        self.rows = m
        self.columns = n
        if not mtrix:
            self._matrix = [[0 for _ in range(n)] for _ in range(m)]
        else:
            if len(mtrix) != m:
                raise MatrixShapeError()
            self._matrix = mtrix

    def __eq__(self, other):
        """
        Check if two matrices are equal by comparing their
        corresponding rows.
        """
        pass

    def __add__(self, other: Matrix):
        """Add the matrix with another matrix
        by adding their corresponding entries."""
        if self.rows == other.rows and self.columns == other.columns:
            pass
        else:
            raise MatrixDimensionError

    def __mul__(self, other: Matrix):
        """Multiply a given matrix by a matrix other"""
        if self.columns != other.rows:
            raise MatrixDimensionError()
        else:
            return Matrix(self.rows, other.columns)

    def scale(self, c):
        """Scale the matrix by a given constant c"""
        pass

    def transpose(self):
        """Transpose the given m x n matrix."""
        self.rows, self.columns = self.columns, self.rows

    def row_reduce(self):
        """Row-Reduce the given matrix"""
        pass


class ZeroMatrix(Matrix):
    """"""

    def __init__(self, m, n):
        Matrix.__init__(self, m, n)


class SquareMatrix(Matrix):
    """An identity matrix class"""

    def __init__(self, n):
        Matrix.__init__(self, n, n)

    def is_symmetric(self):
        """Check if the matrix is symmetric"""
        pass

    def is_skew_symmetric(self):
        """Check if the matrix is skew-symmetric"""
        pass

    def is_invertible(self):
        """Check if the matrix is invertible."""
        pass


class IdentityMatrix(SquareMatrix):
    """An identity matrix class"""

    def __init__(self, n):
        SquareMatrix.__init__(self, n)


class Row(Matrix):
    """A Row """
    def __init__(self, n: int):
        Matrix.__init__(self, 1, n)

    def __mul__(self, other: Column):
        """Multiply the given row by a column"""
        pass


class Column(Matrix):
    """A Column """

    def __init__(self, n):
        Matrix.__init__(self, n, 1)

    def __mul__(self, other: Row):
        """Multiply the given Column by a Rows"""
        pass


class Equation:
    """Initialize a new equation"""
    def __init__(self) -> None:
        """Initialize a new equation"""
        pass


def convert_to_ax_equal_b_form(equation: Equation):
    pass


A = Matrix(3, 2)
B = Matrix(3, 2)
C = Matrix(2, 2)
b = Matrix(2, 1)

# print(A * B * C)
