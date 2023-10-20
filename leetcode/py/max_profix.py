class Solution:
    def maxProfit(self, prices):
        res = 0
        lowest = prices[0]
        for day in prices:
            if day < lowest:
                lowest = day
            res = max(res, day-lowest)
        return res