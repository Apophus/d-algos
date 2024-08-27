import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #turn the nums to negative to create a reverse
        _nums = [-num for num in nums]
        heapq.heapify(_nums)
        while k > 0:
            heapq.heappop(_nums)
            k -=1

        return abs(heapq.heappop(_nums))


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

class Solution:
    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums, k):
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

class Solution:
    def findKthLargest(self, nums, k):
        # Initialize an empty list
        k_numbers_min_heap = []

        # Add first k elements to the list
        for i in range(k):
            k_numbers_min_heap.append(nums[i])

        # Convert the list into a min-heap
        heapq.heapify(k_numbers_min_heap)

        # Loop through the remaining elements in the 'nums' array
        for i in range(k, len(nums)):
            # Compare the current element with the minimum
            # element (root) of the min-heap
            if nums[i] > k_numbers_min_heap[0]:
                # Remove the smallest element
                heapq.heappop(k_numbers_min_heap)
                # Add the current element
                heapq.heappush(k_numbers_min_heap, nums[i])

        # The root of the heap has the Kth largest element
        return k_numbers_min_heap[0]