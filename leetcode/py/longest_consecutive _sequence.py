class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num -1 not in nums_set:
                length =1 
                while num + length in nums_set:
                    length +=1 
                    
                longest = max(length, longest)
                
        return longest




if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    sol = Solution()
    print(sol.longestConsecutive(nums))