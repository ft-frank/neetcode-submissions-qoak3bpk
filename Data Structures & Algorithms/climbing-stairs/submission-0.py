class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def climb(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            elif n == 2:
                return 2
            result = climb(n-1) + climb(n-2)
            
            memo[n] = result
            return result
        return climb(n)