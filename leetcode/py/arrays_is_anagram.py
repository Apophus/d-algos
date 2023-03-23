from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = Counter(s)
        t_count = Counter(t)

        return True if s_count == t_count else False


