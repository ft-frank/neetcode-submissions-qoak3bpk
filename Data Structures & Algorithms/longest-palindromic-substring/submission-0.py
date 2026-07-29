"""
Word:ababd

We understand for palindromic questinos we must have O(n^2) time complexity, because we must look through every single
index i and j pairing. However without DP, we have an additional O(n) isPalindrome function. Instead we use dynamic programming to make
palindrome search O(1).


We must find a recurrence relationship in palindromes.

It is.

if the leftmost character == rightmost character, and the substring in between is equal, then palindrome





"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = resLen = 0

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1): #A pattern we should remember, go back to front, so that when we compute dp[i][j], value dp[i+1][j-1] known. 
                                     #We can kind of figure out that i should go backwards, j forwards.
            for j in range(i, n):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        resIdx = i
                    


        return s[resIdx:resIdx + resLen]