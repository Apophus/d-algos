class Solution:
    def twoSum(self, nums, target):
        res = []
        if len(nums) == 2:
            res = [0, 1]
            return res
        for index, num in enumerate(nums):
            other = target - num
            if other in nums[index + 1:]:
                other_index = nums[index + 1:].index(other)
                res.append(index)
                res.append(other_index+index+1)
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4],6))
