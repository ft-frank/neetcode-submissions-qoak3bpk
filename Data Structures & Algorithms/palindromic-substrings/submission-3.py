class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]

        """
        A DP matrix, that represents if a substring between any two indices is palindromic
        """

        for i in range(n-1, -1, -1): #Going backwards from last character
            for j in range(i, n): #Going from current char to end
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1

        return res
     
        """
        O(n^2) nested loop, iterating through every substring. usually you would have to check if each was a palindrome, which would take 
        an EXTRA O(n), however if we use DP, we store if a smaller substring is a palindrome, and therefore it takes O(1) time each step to calculate if 
        if a substring is palindrome. 

        Therefore O(n^2)

        """