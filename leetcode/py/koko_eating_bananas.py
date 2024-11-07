import math
class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        res = right
        while left <= right:
            rate = (left+right)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
                
            if hours <= h:
                res = min(res, rate)
                right = rate - 1
            else:
                left = rate + 1
                
        return res