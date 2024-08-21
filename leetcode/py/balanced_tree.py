class TreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):

        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and (abs(left-right) <=1)
            return [balanced,1+(max(left[1], right[1]))]

        return dfs(root)[0]
