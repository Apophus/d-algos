class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid_point = (end + start)//2
            if nums[mid_point] > target:
                end = mid_point - 1
            elif nums[mid_point] < target:
                start = mid_point + 1
            else:
                return mid_point
        return -1