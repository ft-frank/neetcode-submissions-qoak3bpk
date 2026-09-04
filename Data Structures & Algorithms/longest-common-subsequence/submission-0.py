"""
Dynamic Programming.

We iterate through each strings with two pointers.
We calculate if they are the same character, if they are, increment both pointers.

If they aren't the same, then we split into different decision trees, one where we incremented the pointer on first, and one where we incremented the point on second. 

We use 2D memoisation to be able to avoid redundant calculations.
That is why this questions is within the 2D dynamic-programming section

E.G
cat
crabt
Answer should be 3



  
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[None] * len(text2) for _ in range(len(text1))] #The index of text2 is the columns. #The index of text1 is which row

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[i][j]:
                return dp[i][j]

            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res =  max(dfs(i + 1, j), dfs(i, j + 1))
            dp[i][j] = res
            return res

        return dfs(0, 0)









        
