# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None
        # swap children
        root.left, root.right = root.right, root.left
        
        # make 2 recursive calls to swap children left and right.
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root