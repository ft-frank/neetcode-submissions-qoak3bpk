class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        The total summation is the max amount that an array nums can go. Therefore we must also flip in the other direction as well for negative.
        """
        dp = [[None]* (sum(nums) * 2 + 1) for n in nums] #each row is index, each column is a certain amount
        
        def dfs(i, amount):
            res = 0
            if i >= len(nums) and amount == target: #if used all coins and amount = target
                return 1
            elif i >= len(nums):
                return 0
            elif dp[i][amount] is not None:
                res = dp[i][amount]
            else:
                res += dfs(i + 1, amount + nums[i])
                res += dfs(i + 1, amount - nums[i])
            dp[i][amount] = res
            return res

        return dfs(0, 0)
            


"""
You have to use all coins within the array, therefore we only check if our amount is == target once index is after length of nums.
What are we DPing?
At every point, we choose to add or subtract. Therefore it is inevitable that we reach the same point many times.

E.g

For example 1.

Line 1 -> + 2, -2
Line 2 -> -2, +2

They reach the same (index = 2, amount = 4). If line 1 calculates 0 ways, then line 2 has 0 ways. If line 1 calculates 1 way, then for line 2 we add 1 more way.

"""