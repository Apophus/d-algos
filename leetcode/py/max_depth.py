from collections import deque


class Solution:
    def maxDepth(self, root):
        """Solution recursively
        Args:
            root (_type_): _description_
        Returns:
            int: max depth of tree
        """
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
    
    def bfs(self, root):
        """Solution with breadth first search
        Args:
            root (root node): root node
        Returns:
            level: maximum depth of tree
        """
        if not root:
            return 0
        
        level = 0 
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1
        return level
    
                