class Solution:
    def removeDigit(self, number, digit):
        maximize = ''
        for index, num in enumerate(number):
            if num == digit:
                current = number[:index] + number[index+1:]
                
                if maximize == "" or current > maximize:
                    maximize = current 
        return maximize
