class Solution:
    def minWindow(self, s, t):
        if t == "": return ""
        requirements = {}
        for _char in t:
            requirements[_char] = 1 + requirements.get(_char, 0)
        
        left = 0
        window = {}
        have, need = 0, len(requirements) 
        res, _shortest = [-1,-1], float('infinity')
        
        for right, letter in enumerate(s):
            window[letter] = window.get(letter, 0) + 1 
            
            if letter in requirements and window[letter] == requirements[letter]:
                have += 1
                
            while have == need:
                if (right - left +1 ) < _shortest:
                    
                    res = [left, right]
                    _shortest = (right-left+1)
                    
                window[s[left]] -= 1 
                if s[left] in requirements and window[s[left]] < requirements[s[left]]:
                    have -= 1
                left +=1
                
            
        return s[res[0]:res[1]+1] if _shortest != float('infinity') else '' 