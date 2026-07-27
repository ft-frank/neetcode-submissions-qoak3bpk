class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def climb(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1:
                return 0
            res = min(climb(n-1) + cost[n-1], climb(n-2) + cost[n-2])
            memo[n] = res
            return res
        return climb(len(cost))
        
