class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i==len(candidates):
                return
            #decision to include
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            #decision to exclude
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, total+candidates[i+1])
        dfs(0, [], 0)
        return res