


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
                res.append(cur.copy())

            for i in range(l , r + 1):
                if isPalindrome(l, i):
                    cur.append(s[l: i + 1])
                    backtrack(i + 1, r, cur)
                    cur.pop()
                    

        
        backtrack(0, len(s) - 1, [])
        return res


"""
Problem here is that when I have two characters left that are not the same, I explore both of them, but that obviously fails. 



"""