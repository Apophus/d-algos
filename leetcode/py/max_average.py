class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = float('-inf')
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]

        res = max(res, float(curr_sum / k))

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            res = max(res, curr_sum / k)

        return res
