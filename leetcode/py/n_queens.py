class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.']*n for _ in range(n)]
        columns = set()
        positive_diagonal = set() #(r+c)
        negative_diagonal = set() #(r-c)
        
        res = []
        
        def backtrack(row):
            if row == n:
                copy = [''.join(_row) for _row in board]
                res.append(copy)
                return
            
            for column in range(n):
                if column in columns or row + column in positive_diagonal \
                or row - column in negative_diagonal:
                    continue
                
                columns.add(column)
                board[row][column] = 'Q'
                positive_diagonal.add(row+column)
                negative_diagonal.add(row-column)
                
                backtrack(row+1)
                
                columns.remove(column)
                board[row][column] = '.'
                positive_diagonal.remove(row+column)
                negative_diagonal.remove(row-column)
                
        backtrack(0)
        
        return res
    

class Solution2(object):
    def solveNQueens(self, n):
        board = [['.']*n for _ in range(n)]
        res = []
        
        def backtrack(row):
            if row == n:
                copy = [''.join(_) for _ in board]
                res.append(copy)
                
            for column in range(n):
                if self.is_safe(row, column, board):
                    board[row][column] = 'Q'
                    backtrack(row+1)
                    board[row][column] = '.'
        backtrack(0)
        return res
    
    def is_safe(self, row, column, board):
        _row = row -1
        
        #check columns
        while _row >= 0:
            if board[row][column] == 'Q':
                return False
            _row -= 1
        
        _row, _column = row -1, column - 1
        while _row>=0 and _column>=0:
            if board[_row][_column] == 'Q':
                return False
            _row -= 1
            _column -= 1
            
        _row, _column = row - 1, column +1
        while _row>=0 and _column<len(board):
            if board[_row][_column] == 'Q':
                return False
            _row -= 1
            _column += 1
            
        return True