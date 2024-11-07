import heapq
class MedianFinder(object):

    def __init__(self):
        self.stream = []
        heapq.heapify(self.stream)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.stream, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.stream)%2:
            mid_point = len(self.stream) // 2
            for i in range(mid_point):
                heapq.heappop(self.stream)
            return heapq.heappop(self.stream)

        mid_point = len(self.stream) // 2
        for i in range(mid_point-1):
            heapq.heappop(self.stream)
        _first = heapq.heappop(self.stream)
        _second = heapq.heappop(self.stream)
        return float((_first+_second)/2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()