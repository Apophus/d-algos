class Solution:
    def trap(self, heights):
        if not heights: return 0
        
        left, right = 0, len(heights)
        leftMax, rightMax = heights[left], heights[right]
        res = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, heights[left])
                res += leftMax - heights[left]
                
            else:
                right -= 1
                rightMax = max(rightMax, heights[right])
                res += rightMax - heights[right]
                
        return res
    