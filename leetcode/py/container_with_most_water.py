class Solution:
    def maxArea(self, hieghts):
        left, right = 0, len(hieghts) - 1
        largest_area = 0
        
        while left < right:
            current_area = min(hieghts[left], hieghts[right])*(right-left)
            largest_area = max(largest_area, current_area)
            # we move the smaller pointer
            
            if hieghts[left] < hieghts[right]:
                left += 1
            right -= 1
        return largest_area