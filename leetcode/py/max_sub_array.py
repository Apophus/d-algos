class Solution:
    def maxSubArray(self, nums):
        
        if len(nums) == 1:
            return nums[0]
        
        _largest_sub = nums[0]
        current_sum = 0
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            _largest_sub = max(_largest_sub, current_sum)
            
        return _largest_sub
        
        