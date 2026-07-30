"""
Integer array nums.

Valid: 1, 2, 3, 4, 5, 6, 7, 8, 9




"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        n = len(nums)

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n-1:
                return 1
            res = 1
            for j in range(i, n):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j)) #count 1 towards the subsequence
            memo[i] = res
            return memo[i]
        return max(dfs(i) for i in range(n))
            