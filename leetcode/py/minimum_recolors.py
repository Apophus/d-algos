class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left, min_operations, _count, flips = 0, float('inf'), 0, 0
        for right in range(len(blocks)-1):
            if blocks[right] == 'W':
                flips += 1

            _count += 1

            if _count == k:
                min_operations = min(flips, min_operations)
                if blocks[left] == 'W':
                    flips -=1

                _count -=1
                left +=1
        return min_operations

if __name__ == '__main__':
   blocks =  "WBBWWBBWBW"
   res = Solution()
   print(res.minimumRecolors(blocks, 7))

