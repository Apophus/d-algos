import heapq
from collections import Counter, deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        char_map = Counter(tasks)
        max_heap = [-c for c in char_map.values()] #negate to invert values for the minheap
        heapq.heapify(max_heap)
        q = deque() #pairs of curr and next time we revisit
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                curr = 1 + heapq.heappop(max_heap)
                if curr:
                    _next_time = n + time
                    q.append((curr, _next_time))

            if q and q[0][1] == time:
                # add the element back to the heap
                heapq.heappush(max_heap, q.popleft()[0])

        return  time


