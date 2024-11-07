class Solution:
    def findClosestNumber(self, nums):
        smallest = nums[0]
        
        for num in nums:
            if abs(num) < abs(smallest):
                smallest = num
        
        return abs(smallest) if smallest < 0 and abs(smallest) in nums else smallest
        
        