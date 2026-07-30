"""
We have a recursive function nacci(n).

nacci(n) will

check base cases T0 = 0, T1 = 1, T2 = 1
else:
    compute Tn+3.
memoise Tn+3



"""


class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        memo = {}

        def nacci(n):

            if n in memo:
                return memo[n]

            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 1

            memo[n] = nacci(n-3) + nacci(n-2) + nacci(n-1)

            return memo[n]
        return nacci(n)
