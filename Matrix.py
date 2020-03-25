# Alekseeva Elena


class Matrix:
    """Matrix data type
       A class that represents the [n x n] - matrix
    """

    def __init__(self, n, data=0):
        """Initializes a matrix.
        """
        self._nrow, self._ncol = n, n
        self._data = 0, 0, []
        self.data = data
        self.rows = [[self.data] * self._nrow for _ in range(self._ncol)]

    def __str__(self):
        """Function returns the matrix string representation.
        """
        return "\n".join(map(str, self.rows))

    def __repr__(self):
        """Function returns the matrix representation.
        """
        return f'{self.__class__.__name__}({self._nrow!r}, {self._ncol!r})'

    def __eq__(self, other):
        """Checks whether a given matrix is equal to another one"""
        return isinstance(other, Matrix) and self._nrow == other._nrow \
               and self._ncol == other._ncol and self._data == other._data


# Test
myMat_1 = Matrix(2, data=2)
myMat_2 = Matrix(2, data=2)
print(myMat_1.__str__())
print(myMat_2.__str__())
print(myMat_1 == myMat_2)
