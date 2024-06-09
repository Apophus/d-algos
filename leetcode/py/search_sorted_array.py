class Solution:
    def search(self, nums, target):
        
        left, right = 0, len(nums) -1
                
        while left <= right:
            mid = (right + left)//2
            
            if nums[mid] == target:
                return mid
            #check the left sorted half
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # go left
                    right = mid - 1
                else:
                    #go right
                    left = mid + 1
                    
            else:
                if nums[mid] < target <= nums[right]:
                    #go right
                    left = mid + 1 
                    
                else:
                    #go left 
                    right = mid - 1
                    
            
        return -1
    
                    
            
                
                
[4,5,6,7,0,1,2]

[0,1,2,4,5,6,7]
[6,7,0,1,2,4,5]