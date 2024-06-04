# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, sub_root):
        if not root: return False
        if not sub_root: return True
        
        if self.same_tree(root, sub_root):
            return True
        left = self.isSubtree(root.left ,sub_root)
        right =  self.isSubtree(root.right, sub_root)
        return left or right
    
    def same_tree(self, root, sub_root):
        if not root and not sub_root:
            return True
        
        if (root and sub_root) and root.val == sub_root.val:
            left = self.same_tree(root.left, sub_root.left)
            right = self.same_tree(root.right, sub_root.right)
            return left and right
        return False
        