class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, res, curr_sum= 0,float('inf'), 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            res += 1

            while curr_sum >= target:
                res = min(res, right-left+1)
                curr_sum -= nums[left]
                left += 1

        return  res if res< float('inf') else 0

