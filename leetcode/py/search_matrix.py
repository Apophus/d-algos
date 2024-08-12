class Solution:
    def searchMatrix(self, matrix, target):
        start, end = 0, len(matrix) -1
        
        while start <= end:
            mid = (end + start)//2
            
            if target > matrix[mid][-1]:
                start = mid + 1 
            elif target < matrix[mid][0]:
                end = mid -1
            else:
                break
        
        if not start <= end:
            return False
        
        row = (end + start) // 2
        
        left, right  = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (right + left) //2 
            if target > matrix[row][mid]:
                left = mid + 1
                
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
                