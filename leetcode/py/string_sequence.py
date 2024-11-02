class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        res = ['a']
        i = 0
        j=0
        while res[-1] !=target:
            if res[-1][j] == target[i]:
                res.append(res[-1][:j+1]+'a')
                j+1
                i+1
            else:
                res.append(res[-1][:j]+chr(ord(res[-1][j])+1))
        return res
                
        