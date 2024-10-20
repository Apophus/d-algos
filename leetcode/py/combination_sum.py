class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            #decision to include
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            #decision to exclude
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
