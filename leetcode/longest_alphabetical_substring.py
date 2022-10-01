class Solution(object):
    def longestContinuousSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        res = 0
        count = 1

        for i in range(len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                count += 1
                res = max(count, res)
            else:
                count = 1

        return max(res, count)


