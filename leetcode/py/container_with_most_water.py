class Solution:
    def maxArea(self, height):
        _max_area = 0
        left, right = 0, len(height)
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            _max_area = max(_max_area, area)
            
            if height[left] < height[right]:
                left += 1
                
            else: 
                right -= 1
            
        return _max_area