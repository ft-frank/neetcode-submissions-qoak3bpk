class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        convert = {

            '2': "abc",
            '3': "def",
            '4': "ghi", 
            '5': "jkl",
            '6':"mno",
            '7':"pqrs",
            '8': "tuv",
            '9': "wxyz"


        }

        digits = str(digits)


        res = []

        if len(digits) == 0:
            return res

        def dfs(i, cur):

            if len(cur) == len(digits):
                res.append("".join(cur))
                return

            for j in convert[digits[i]]:

                cur.append(j)
                dfs(i + 1, cur)
                cur.pop()
        dfs(0, [])
        return res
            
