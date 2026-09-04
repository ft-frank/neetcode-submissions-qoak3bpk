"""
Now I need to include a dynamic programming solution

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [[None] * 2 for p in prices] #each row is index. each col is True holding, or False holding

        def dfs(i, holding):
            if i>= len(prices):
                return 0
            col = int(holding)
            res = 0
            if dp[i][col]:
                return dp[i][col]
            elif not holding:
                res = max(-prices[i] + dfs(i+1, True), dfs(i+1, False))
            else:
                res =  max(prices[i] + dfs(i + 2, False), dfs(i + 1, True))
            dp[i][col] = res
            return res

        return dfs(0, False)
