# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        res = 0
        stack = []
        curr_node = root
        
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            res += 1
            if res == k:
                return curr_node.val
            curr_node = curr_node.right
            
    
        def inOrderTraversal(self, node, k):
            """In order tree traversal

            Args:
                node (TreeNode): node that's being processed.
                k (int): kth value

            Returns:
                int: TreeNode.val
            """
            if not node or k==res:
                return
            #go left
            self.inOrderTraversal(node.left, k)
            res += 1
            
            if res == k:
                return node.val
            
            self.inOrderTraversal(node.right, k)
            
        