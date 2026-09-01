"""


Dynamic Programming Question.

To use dynamic programming for palindromes we can apply this rule:

When a string is a palindrome, such as aa. How can we remember that it is a palindrome, to see if adding characters results in a palindrome?

e.g baabb

We check b and b. (0 and 4). True.
We check a and b. We already checked aab. Therefore it is false. therefore 0 and 4 is false. 
We have to use a matrix to keep track whether the substring between two indices results in a palindrome. 

OR


If we regard as a backtracking question. 

We have aab.

We take a. We check if it is a palindrome. It is so we have two options, move onto aa, or add a and move onto a again. 
For the case of taking aab, we still have a character cooking, but its not valid by the time we reach end of string. Therefore the cur, can never be valid and we don't append. 


beggar

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
         
        cur = []
        res = []

        def backtrack(l, r, cur):
            if l > r:
                res.append(cur.copy())
                return
            
            for i in range(l, r+1):
                if isPalindrome(l, i):
                    cur.append(s[l:i + 1])
                    backtrack(i + 1, r, cur)
                    cur.pop()

            

            
        backtrack(0, len(s) - 1, cur)

        return res


