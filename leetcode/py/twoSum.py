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

class SolutionII:
    def twoSum(self, nums, target):
        
        nums_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                return [nums_map[diff],index]
            nums_map[num] = index
        
    

if __name__ == '__main__':
    s = SolutionII()
    print(s.twoSum([2,7,11,15],9))
