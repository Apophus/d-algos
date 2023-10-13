"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Solution requires a dict and stack.

"""
from collections import Counter

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        char_map = {'(': ')',
                    '{': '}',
                    '[': ']'
                    }
        stack = []

        for char in s:
            if char in char_map.keys():
                stack.append(char)
                continue

            if not stack or char != char_map[stack[-1]]:
                return False
            stack.pop()

        return not stack



if __name__ == '__main__':
    s = '([]{})'
    s1 = '()[]{}'
    s2 = '()[{}]'
    s3 = "([)]"
    sol = Solution()
    print(sol.isValid(s))