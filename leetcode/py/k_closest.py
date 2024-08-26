import heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        k_closest = []
        for point in points:
            res = [(point[0]**2 + point[1]**2), point[0],point[1]]
            distances.append(res)

        heapq.heapify(distances) #shall sort by first element of the list
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            k_closest.append([x,y])

        return k_closest
