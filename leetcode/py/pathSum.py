class Solution:
    def hasPathSum(self, root, target):
        
        def dfs(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            if not node.left and not node.right:
                return currSum == target
            
            left = dfs(node.left, currSum)
            right = dfs(node.right, currSum)
            
            return left or right
        return dfs(root, 0)