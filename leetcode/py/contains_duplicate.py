class Solution:
    def containsDuplicate(self,nums):
        
        if len(set(nums)) == len(nums):
            return False
        return True