class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right