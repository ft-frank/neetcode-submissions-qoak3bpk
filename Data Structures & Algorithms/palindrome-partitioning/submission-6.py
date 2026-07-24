


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []


        def isPalindrome(l, r):

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True


        def backtrack(l, r, cur):
            if l > r:
                res.append(cur.copy()) #l pointer passed r pointer

            for i in range(l , r + 1): 
                if isPalindrome(l, i): #check if palindrome from l to i, and if so, then now we check from i to the end for more palindromes, then which we append once we reach the end, and then return back to here
                    cur.append(s[l: i + 1])
                    backtrack(i + 1, r, cur)
                    cur.pop()


        
        backtrack(0, len(s) - 1, [])
        return res


"""
Problem here is that when I have two characters left that are not the same, I explore both of them, but that obviously fails. 



"""