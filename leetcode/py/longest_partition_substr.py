class Solution:
    def partition_string(s):
        count, partition = 0, ''

        for char in s:
            if char in partition:
                count += 1
                partition = ''
            partition += char

        return count + 1
