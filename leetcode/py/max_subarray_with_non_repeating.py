class Solution:
    def solution(self, s):
        left, res = 0, 0
        seen = set()
        for i in range(len(s)):
            while (s[i]) in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            res = max(res, i - left+1)
        return  res