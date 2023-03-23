"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        word_counts = {}

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in word_counts:
                word_counts[sorted_word].append(word)
                continue
            word_counts[sorted_word] = [word]
            continue

        for words in word_counts:
            result.append(word_counts[words])

        return result

