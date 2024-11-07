class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for index, number in enumerate(nums):
            #skip duplicates
            if index > 0 and number == nums[index-1]:
                continue
            #initialize pointers
            left, right = index+1, len(nums)-1
            while left < right:
                three_sum = number + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([number, nums[left], nums[right]])
                    left +=1
                    #ignore duplicates
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                        
                
        return res