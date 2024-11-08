# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    This guy explains it better: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram
    """
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = [root.val]
        def dfs(root):
            if not root: return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val + left_max + right_max)

            return root.val + max(left_max, right_max)
        dfs(root)
        return res[0]

