from collections import deque

class Solution:
    def numIslands(self, grid):
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, columns = len(grid), len(grid[0])
        islands = 0
        visited = set()


        def bfs(row,column):
            queue = deque()
            visited.add((row, column))
            queue.append((row, column))
            
            while queue:
                curr_row, curr_column = queue.popleft()
                for row_dir, col_dir in direction:
                    _row, _column = curr_row+row_dir, curr_column+col_dir
                    
                    if (_row in range(rows) and 
                        _column in range(columns) and
                        grid[_row][_column] == '1' and
                        (_row, _column) not in visited
                        ):
                        queue.append((_row, _column))
                        visited.add((_row, _column))
            
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1' and (row, column) not in visited:
                    bfs(row, column)
                    islands += 1
                        
        return islands
