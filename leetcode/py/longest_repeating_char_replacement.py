class Solution:
    def characterReplacement(self, s, k) :
        left, _max_length = 0, 0
        char_count = {}
        
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            if (right - left +1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
                
            _max_length = max(_max_length, right-left+1)
        return _max_length    