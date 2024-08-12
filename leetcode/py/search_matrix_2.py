class Solution:
    def searchMatrix(self, matrix, target):
        row, column = 0, len(matrix[0]) - 1
        
        while (column >= 0 and row < len(matrix)):
            if matrix[row][column] == target:
                return True
            elif target > matrix[row][column]:
                row += 1
            else:
                column -= 1
                
        return False