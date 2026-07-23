"""
1, 2, 2, 3, 5, 6, 9



"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        subset = []

        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif sum(subset) > target:
                return
            if i >= len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1)
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res


