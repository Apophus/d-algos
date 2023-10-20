class Solution:
    def isValidSudoku(self, board):
        print(self.validate_boxes(board), self.validate_columns(board), self.validate_rows(board))
        if all([self.validate_boxes(board), self.validate_columns(board), self.validate_rows(board)]):
            return True
        return False
        
    def validate_rows(self, board):
        
        for row_index, row in enumerate(board):
            for column_index, column in enumerate(board[row_index]):
                if not column.isdigit():
                    continue
                if not (1>= int(column) <10 ) and column in board[row_index][column_index+1:]:
                    return False
                
        return True

    def validate_columns(self, board):
        
        for column in range(len(board)-1):
            curr_column = []
            for row in range(len(board)-1):
                if not board[column][row].isdigit():
                    continue
                curr_column.append(board[column][row])
                
            if len(set(curr_column)) == len(curr_column):
                continue
            else:
                return False
        return True
        
    def validate_boxes(self, board):
        
        for row in range(3):
            for column in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        val = board[3*row+i][3*column+j]
                        if not val.isdigit():
                            continue
                        box.append(val)
                if len(set(box)) != len(box):
                    return False
        return True

import collections

class Solution1:
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


if __name__ == "__main__":
    board = [[".",".","4",".",".",".","6","3","."],
             [".",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".","9","."],
             [".",".",".","5","6",".",".",".","."],
             ["4",".","3",".",".",".",".",".","1"],
             [".",".",".","7",".",".",".",".","."],
             [".",".",".","5",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]
    sol = Solution()
    print(sol.isValidSudoku(board=board))