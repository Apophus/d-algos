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


def no_zeros_rows(board):
    """
    validate that the whole board doesn't
     contain zeros
    """
    for row in board:
        if 0 in row:
            break

            return False
    return True


def get_rows(board):
    return board


def get_columns(board):
    """Take board and create a list of cloumns"""
    columns = [[] for i in range(9)]
    for i in board:
        for j in range(9):
            columns[i].append(board[i][j])

    return columns


def get_block(board, part):
    ll = []
    for i in range(part, part + 3, part):
        for k in range(3):
            l = board[i][k]
            ll.append(l)
    return ll


def get_all_blocks(board):
    blocks = [[] for i in range(9)]

    return blocks


def contains_all_digits_rows(board):
    ...


def contains_all_digits_rows(board):
    ...


def contains_all_digits_blocks(board):
    ...


def valid_solution(board):
    check = "123456789"
    #
