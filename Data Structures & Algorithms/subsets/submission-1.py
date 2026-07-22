class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i]) # we want to include this character
            dfs(i + 1)
            subset.pop()
            dfs(i + 1) # we don't want to include this character

        dfs(0)
        return res