class Solution:
    def twoSum(self, numbers, target):
        """This is meant to work with 
        a strictly-increasing sequence

        Args:
            numbers (numbers): list
            target (target): int

        Returns:
            _type_: _description_
        """
        left, right = 0, len(numbers)-1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                return [left+1, right+1]

if __name__ == '__main__':
    s = [5,25,75]
    sol = Solution()
    print(sol.twoSum(s, 100))