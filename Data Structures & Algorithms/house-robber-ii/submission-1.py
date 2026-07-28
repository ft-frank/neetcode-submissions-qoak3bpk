"""
We reocgnise the only difference in House Robber II to House Robber,
is that if we choose to rob the first house, we also cannot choose to rob the last house.
That is the only changed decision.

Therefore we will choose to do a top-down dynamic programming approach, with a 
DP array.

Using this DP array, we use memo to cache the computations for a subproblem incluing the first house, and then
without including the first house, which makes things alot different

Our general formula would look something like:

memo = [[-1]*2 for _  in range(len(nums))]
def dfs(i, flag):
    if i >= len(nums) or (flag == 1 and i >= len(nums) - 1):
        return 0
    elif memo[i][flag] != -1:
        return memo[i][flag]
    memo[i][flag] = max(dfs(i + 1, flag), dfs(i + 2, flag or i == 0))
    return memo[i][flag]




"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        memo = [[-1]*2 for _  in range(len(nums))]
        def dfs(i, flag):
            if i >= len(nums) or (flag == 1 and i >= len(nums) - 1):
                return 0
            elif memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))