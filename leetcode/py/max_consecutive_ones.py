class Solution:
    def longestOnes(self, nums, k):
        
        left, _max_length, zeros = 0, 0, 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -=1
                left +=1
                
            _max_length = max(_max_length, right-left+1)
                                    
        return _max_length                
            
            
        