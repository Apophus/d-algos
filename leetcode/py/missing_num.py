class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = len(nums)

        for i in range(0, top+1):
            print(i)
            if i not in nums:
                return i 

sol = Solution()
nums = [0,1]

print(sol.missingNumber(nums))