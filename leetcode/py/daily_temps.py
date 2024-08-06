class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        
        for day, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                _temp, _day = stack.pop()
                res[_day] = day - _day
                
            stack.append([temperature, day])
            
        return res