class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for i in operations:
        
            if i == '+':
                last, second_last = stack[-1], stack[-2]
                score = last + second_last
                stack.append(score)
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                last_score = stack.pop()
                stack.append(last_score*2)
                
            stack.append(i)
        return sum(stack)