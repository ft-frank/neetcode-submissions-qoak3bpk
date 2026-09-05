"""
So we iterate through word1 and word2. 
Our DP is a 2D DP that memoises index of word1 and index of word2.

At each decision, we have 3 ways to do something.
Insert, Delete / Replace.

To perform the MINIMUM number of operations, we choose the most optimal one. 
When is each most optimal?

Insert -> word1 needs more letters to fill length of word2, and missing character
Replace -> word1 doesn't need more letters to fill length of word2, and missing character
Delete -> word1 has too many letters, and the character isn't necessary

We increment up the index of word2 as we verify that we have the letters necessary to be able to fill them.

e.g

mon
mon. Match up

therefore at 
k and e. We can do a replace? or a delete or an insert. We try all 3 options.
Then once we reach end of money, return how many operations it took.

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[None] * (len(word2) + 1) for c in range(len(word1) + 1)] #each row represents an index in word 1. each col represents an index in word 2.

        
        def dfs(i, j):
            res = 0 #no operation yet
            if i >= len(word1) and j >= len(word2): #if have moved past all characters
                return 0
            elif i >= len(word1):
                return len(word2) - j
            elif j >= len(word2):
                return len(word1) - i
            elif dp[i][j] is not None:
                return dp[i][j]
            elif word1[i] == word2[j]:
                res = dfs(i + 1, j + 1) #don't add 1, no need for operation
            else: #try all three operations
                insert = 1 + dfs(i, j+ 1)
                deletion = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                res = min(insert, deletion, replace)
            dp[i][j] = res
            return res
        return dfs(0, 0)

