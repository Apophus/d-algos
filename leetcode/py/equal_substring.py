class Solution:
    def equalSubstring(self, s, t, maxCost):
        #diff = [abs(ord(s[_]) - ord(t[_])) for _ in range(len(s)-1)]
        currCost = 0
        left = 0
        res = 0
        
        for right in range(len(s)):
            currCost += abs(ord(s[right]) - ord(t[right]))
            
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                
            res = max(res, right-left+1)
            
        return res