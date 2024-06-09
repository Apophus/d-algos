class Solution:
    def search(self, nums, target):
        
        left , right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            #checking the left sorted side
            if nums[mid] <=target:
                if nums[left] <= target < nums[mid]:
                    #go right
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] < target <= nums[right]:
                    # go left
                    right = mid - 1
                else:
                    #go right 
                    left = mid + 1
                    
        return False