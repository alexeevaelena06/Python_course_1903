# Alekseeva Elena


class Matrix:
    """Matrix data type
       A class that represents the [n x n] - matrix
    """

    def __init__(self, n, data=0):
        """Initialize a matrix.
        """
        self._nrow, self._ncol = n, n
        self.data = data
        self.rows = [[self.data] * self._nrow for _ in range(self._ncol)]

    def __str__(self):
        """Return the matrix string representation.
        """
        return "\n".join(map(str, self.rows))

    def __repr__(self):
        """Return the matrix representation.
        """
        return f'{self.__class__.__name__}({self._nrow!r}, {self._ncol!r})'

    def __eq__(self, other):
        """Check whether a given matrix is equal to another one"""
        return isinstance(other, Matrix) and self._nrow == other._nrow \
               and self._ncol == other._ncol and self.data == other.data


# Test
myMat_1 = Matrix(2, data=25)
myMat_2 = Matrix(2, data=25)
print(myMat_1.__str__())
print(myMat_2.__str__())
print(myMat_1 == myMat_2)
