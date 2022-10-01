from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)

        if not evens:
            return -1
        even_count = Counter(evens)

        counts = [i for i in even_count.values()]
        most_common = max(counts)
        top = list(sorted([i for i in even_count if most_common == even_count[i]]))

        return top[0]

if __name__ == "__main__":
    nums = [0,1,2,2,4,4,1]

    soln = Solution()
    print(soln.mostFrequentEven(nums))


