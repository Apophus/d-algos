from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_frequency = Counter(nums)
        result = num_frequency.most_common(k)
        return [x[0] for x in result]
