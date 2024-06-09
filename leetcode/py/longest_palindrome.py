class Solution:
    def longestPalindrome(self, s):
        res = ''
        res_length = 0
        for i in range(len(s)):
            left, right = i, i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                 if (right-left +1)> res_length:
                     res = s[left:right+1]