# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Initialize a list to hold the maximum diameter encountered
        self.res = 0
        # Define a recursive function to calculate the diameter
        def diameter(node):
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively calculate the diameter of left and right subtrees
            left = diameter(node.left)
            right = diameter(node.right)

            # Update the maximum diameter encountered so far
            self.res = max(self.res, left + right)

            # Return the depth of the current node
            return max(left, right) + 1

        # Call the diameter function starting from the root
        diameter(root)
        # Return the maximum diameter encountered
        return self.res
