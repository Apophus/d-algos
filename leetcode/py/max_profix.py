class Solution:
    """
    We assume that the first element in the list is the lowest.
    We set a placeholder 0 for when there's no profit to be made(descending sequence)
    Loop through the prices and replace the lowest value with the lowest value.
    """
    def maxProfit(self, prices):
        res = 0
        lowest = prices[0]
        for day in prices:
            if day < lowest:
                lowest = day
            res = max(res, day-lowest)
        return res