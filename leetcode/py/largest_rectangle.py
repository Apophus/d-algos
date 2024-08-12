class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        
        for current_index, height in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] > height:
                _index, _height = stack.pop()
                max_area = max(max_area, _height*(current_index - _index))
                start = _index
            stack.append((start, height))
            
        for index, height in stack:
            max_area = max(max_area, height*(len(heights)- index) )
        return max_area