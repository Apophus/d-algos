# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def valid(node, left, right):
            """Function to check recursively if a subtree is valid

            Args:
                node (TreeNode): Root node or parent node
                left (_type_): value of the left child
                right (_type_): value of the right child

            Returns:
                _type_: _description_
            """
            if not node:return True

            if not (left < node.val < right):
                return False
            #check whether the left and right nodes meet the above conditions reccursively
            _left  = valid(node.left, left, node.val)
            _right = valid(node.right, node.val, right)
            return _left and _right
        return valid(root, float('-inf'), float('inf'))
        