from collections import deque
class Solution:
    def rightSideView(self, root):
        res = []
        q = deque([root])
        while q:
            right_side = None
            qLen = len(q)

            for i in range(qLen):
                node =q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                res.append(right_side.val)

        return res