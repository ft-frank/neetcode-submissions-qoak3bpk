"""

What am I memoising in my DP approach?

There comes a scenario where e.g

line 1 -> first (i +1) -> second (j + 1)
line 2 -> second (j + 1) -> first ( i + 1)




"""





class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)] #each row is the j pointer (s1), each col is the k pointer (s2)

        def recurse(i, j, k):
            if i >= len(s3) and j == len(s1) and k == len(s2): #if all pointers reached the end
                return True
            elif i >= len(s3):
                return False
            elif j < len(s1) and k < len(s2) and dp[j][k] is not None:
                return dp[j][k] #would usually be false
            first = False
            second = False
            if j < len(s1) and s3[i] == s1[j]: #is char from the first and from the third the same. 
                first = recurse(i + 1, j + 1, k) 
            if k < len(s2) and s3[i] == s2[k]:
                second = recurse(i + 1, j, k + 1)
            dp[j][k] = first or second
            return first or second
        return recurse(0, 0, 0)
