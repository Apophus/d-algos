class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        charMap = {'2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz'
                    }
        
        def back_track(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in charMap[digits[i]]:
                back_track(i + 1, currStr + c)
        if digits:
            back_track(0, '')
            
        return res
    

if __name__ == '__main__':
    digits = '23'
    res = Solution().letterCombinations(digits)