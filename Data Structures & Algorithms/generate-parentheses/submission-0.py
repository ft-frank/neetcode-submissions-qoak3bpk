

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, ope, remaining):
            if len(cur) == n * 2:
                res.append("".join(cur))
                return
            if ope == 0:
                cur.append('(')
                dfs(cur, ope + 1, remaining - 1)
                cur.pop()
            elif ope + 1 >= remaining:
                cur.append(')')
                dfs(cur, ope - 1, remaining - 1)
                cur.pop()
            else:
                cur.append('(')
                dfs(cur, ope + 1, remaining - 1)
                cur.pop()
                cur.append(')')
                dfs(cur, ope - 1, remaining - 1)
                cur.pop()
        dfs([], 0, n * 2)
        return res