"""
https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

Sudoku is a game played on a 9x9 grid.
The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
so that each column, each row, 
and each of the nine 3x3 sub-grids (also known as blocks)
contain all of the digits from 1 to 9. 

validSolution([
  [5, 3, 4,| 6, 7, 8, |9, 1, 2], 
  [6, 7, 2,| 1, 9, 0, |3, 4, 8],
  [1, 0, 0,| 3, 4, 2, |5, 6, 0],
  __________
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); === False
"""
import pprint


class SodukuSolver:

    def __init__(self, board):
        self.board = board

    def no_zeros_rows(self):
        """
        validate that the whole board doesn't
         contain zeros
        """
        board = self.board

        for row in board:
            if 0 in row:
                return False
        return True

    def get_columns(self):
        """Take board and create a list of columns"""
        columns = [[] for _ in range(9)]
        board = self.board
        for i in range(9):
            for j in range(9):
                columns[i].append(board[j][i])

        return columns

    def get_blocks(self):
        answer = []
        for r in range(3):
            for c in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(self.board[3 * r + i][3 * c + j])
                answer.append(block)
        return answer

    def contains_all_digits(self, arr=None):
        """
        Loops through any 9 arrays and checks the string value against 'check'
        Blocks and rows and columns have 9 arrays
        """
        check = "123456789"
        board = None
        if arr == 'rows':
            board = self.board
        elif arr == 'blocks':
            board = self.get_blocks()
            pprint.pprint(board)
        elif arr == 'columns':
            board = self.get_columns()

        for i in board:
            char_check = list(sorted(i))
            str_check = ''.join(str(_) for _ in char_check)
            if str_check == check:
                continue
            return False
        return True

    def is_valid_solution(self):

        if not self.no_zeros_rows():
            print('no_zeros_rows', False)
            return False
        elif not self.contains_all_digits('rows'):
            print('rows', False)
            return False
        elif not self.contains_all_digits('columns'):
            print('columns', False)
            return False
        elif not self.contains_all_digits('blocks'):
            print('blocks', False)
            return False

        return True


if __name__ == '__main__':
    board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    soduku = SodukuSolver(board)
    print(soduku.is_valid_solution())
