import math


class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        if not (self._validate_dimensions() and self._sqrt_check()):
            print("self._validate_dimensions() and self._sqrt_check()", False)
            return False
        elif not (self._rows_check() and self._squares_check() and self._squares_check()):
            print("self._rows_check() and self._squares_check() and self._squares_check()", False)
            return False

        return True

    def _validate_dimensions(self):
        """Validates if soduku is of the right dimensions"""
        # return False if it's empty
        if not self.data:
            return False
        # check if rows == columns
        for row in self.data:
            if len(row) != len(self.data):
                return False
        return True

    def _sqrt_check(self):
        """
        Checks for the condition: Data structure dimension: NxN where N > 0 and √N == integer
        """

        obj_length = len(self.data)
        sqrt = int(math.sqrt(obj_length))
        return True if sqrt * sqrt == int(obj_length) else False

    def _string_validator(self):
        obj_length = len(self.data)
        str_obj = ''
        for i in range(1, obj_length + 1):
            str_obj += str(i)

        return str_obj

    def _rows_check(self):
        """
        Validates condition: Rows may only contain integers: 1..N (N included)
        """
        for row in self.data:
            row_string = ''.join(str(i) for i in sorted(row))
            if row_string != self._string_validator():
                return False

        return True

    def _columns_check(self):
        """
        Check if columns are valid
        """
        columns = self._get_columns()

        for column in columns:
            column_string = ''.join(sorted(column))
            if column_string != self._string_validator():
                return False
        return True

    def _squares_check(self):
        squares = self._get_squares()
        for square in squares:
            square_str = ''.join(str(i) for i in sorted(square))
            if square_str != self._string_validator():
                return False

        return True

    def _get_columns(self):
        """Take board and create a list of columns"""
        board = self.data
        columns = [[] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                columns[i].append(board[j][i])

        return columns

    def _get_squares(self):

        board = self.data
        squares = []
        block_length = int(math.sqrt(len(board)))
        for r in range(block_length):
            for c in range(block_length):
                block = []
                for i in range(block_length):
                    for j in range(block_length):
                        block.append(board[block_length * r + i][block_length * c + j])
                squares.append(block)
        return squares


if __name__ == '__main__':
    sod = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]

    soln = Sudoku(sod)
    print(soln.is_valid())
