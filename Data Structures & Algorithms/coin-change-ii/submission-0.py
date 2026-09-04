class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[None] * (amount + 1) for c in coins] #each row is an index. #each col is an amount. #a value states is it true that from here can it reach amount

        def dfs(i, cur_amount):
            res = 0
            if i >= len(coins) or cur_amount > amount:
                return 0
            elif dp[i][cur_amount] is not None:
                return dp[i][cur_amount]
            elif cur_amount == amount:
                res = 1
            else:
              
                #include 1 coin if its below amount
                res += dfs(i, cur_amount + coins[i])
                #don't include current coin
                res += dfs(i + 1, cur_amount)
            dp[i][cur_amount] = res
            return res

        return dfs(0, 0)
            
               
            

            