class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        char_set = set()
        res = 0
        
        for index in range(len(s)):
            if s[index] in char_set:
                char_set.remove(s[index])
                left += 1
            char_set.add(s[index])
            res = max(res, index-left+1)
            
        return res
            
        