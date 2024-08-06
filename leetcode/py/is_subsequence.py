class Solution:
    def isSubsequence(self, s, t):
        s_len = len(s)
        t_len = len(t)
        if not s: return True
        if  s_len > t_len: return False
        
        s_index = 0
        for _t in range(t_len):
            if t[_t] == s[s_index]:
                if s_index == s_len -1:
                    return True
                s_index += 1
                
        return False
        