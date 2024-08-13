
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        short, longer = nums1, nums2
        
        if len(short) > len(longer):
            short, longer = longer, short
        
        half = (len(short)+len(longer)) //2
        left, right = 0, len(short) -1
        while True:
            short_mid = (left+right)//2
            """
            pointer for longer array where we expect the median index
            we subtract 2 to offset zero indexing
            """
            mid_point_index = half - short_mid - 2
            
            short_left = short[short_mid] if short_mid >= 0 else float('-infinity')
            short_right = short[short_mid+1] if short_mid +1 < len(short) else float('infinity')
            longer_left = longer[mid_point_index] if mid_point_index >=0 else float('-infinity')
            longer_right = longer[mid_point_index+1] if mid_point_index+1 < len(longer) else float('infinity')
            
            if short_left <= longer_right and longer_left <= short_right:
                #odd cases
                if (len(short)+len(longer)) %2:
                    return min(short_right, longer_right)
                #even cases
                return (max(short_left, longer_left) + min(short_right, longer_right)) /2
            elif short_left > longer_right:
                right  = short_mid - 1
            else:
                left = short_mid + 1
                        