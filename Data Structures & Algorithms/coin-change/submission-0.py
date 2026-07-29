"""
Example:

[3, 5, 6, 7, 8] target = 37 ans = 5

Remaining = 37

Take each coins go down each path

34
32
31
30
29

Then 

go down each path again. 

Finally you will probably repeat a memoisation of something like dfs(26). Since this is repeated, you save the calculation.



"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        n = len(coins)
        if amount == 0:
            return 0

        def dfs(rem): #recommned in 1-D only to include 1 paramater
            if rem in memo:
                return memo[rem]
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            
            mini = float('inf')
            #Try all coins
            for coin in coins:
                res = 1 + dfs(rem - coin)
                mini = min(mini, res)
            
            memo[rem] = mini
            return memo[rem]
        dfs(amount)
        return memo[amount] if memo[amount] < float('inf') else -1
            



            