class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        # [1,1,2,6]
        post_fix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= post_fix
            post_fix *= nums[i]

        return res


