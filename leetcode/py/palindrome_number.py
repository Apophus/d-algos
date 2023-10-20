class Solution:
    
    def isPalindrome(self, x):
        if x < 0:
            return False
        divisor = 1
        while x >= 10*divisor:
            divisor *= 10
            
        while x:
            left, right = x//divisor, x%10
            if left != right: return False
            
            x = (x%divisor) // 10
            divisor = divisor/100
            
        return True