"""
We have a choice to include a character or not to include a character.

Therefore our information we need is index, and the current string we have
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[None] * len(t) for c in s] #Each row is the index i. Each col is the index j.


        def seq(i, j): #i is the pointer to the s string. j is the pointer to the t string.
            if j >= len(t):
                return 1 #it is true that this specific instance you can complete sequence of s
            elif i >= len(s):
                return 0
            elif dp[i][j] is not None:
                return dp[i][j]

            #2 decisions, include char, or not. Can only include if matches j.
            yes = seq(i + 1, j + 1) if s[i] == t[j] else 0
            no = seq(i + 1, j)
            dp[i][j] = yes + no
            return yes + no

        return seq(0, 0)