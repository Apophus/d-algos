class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        item_map = {}
        def populate_item_map(items, item_map):
            for key, value in items:
                if key not in item_map:
                    item_map[key] = value
                else:
                    item_map[key] += value
            return items
        populate_item_map(items1, item_map)
        populate_item_map(items2, item_map)
        res = []
        for key, val in item_map.items():
            res.append([key, val])

        return sorted(res, key=lambda x: x[0])

