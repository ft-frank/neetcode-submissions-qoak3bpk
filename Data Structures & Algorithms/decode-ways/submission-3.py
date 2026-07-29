

class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        count = 0
        n = len(s)
        mapping = {str(d) for d in range(1, 27)}
        # mapping = {chr(ord('A') + s):s +1 for s in range(26)}


        def dfs(i):  
            nonlocal count 
            if i >= n: #is length matching s
                return 1
            if s[i] == '0': #if single char is 0, no way we can continue decoding
                return 0
            if i in memo:
                return memo[i]
            res = dfs(i + 1)
            if i + 2 <= n and s[i:i+2] in mapping: #is 2 char valid, if so run dfs on it
                res += dfs(i+2)     
            memo[i] = res
            return res

        return dfs(0)
                                                           
                                                                       
                                                                        



            
        

            