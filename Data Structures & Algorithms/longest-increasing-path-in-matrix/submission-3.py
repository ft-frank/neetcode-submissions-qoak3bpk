"""
I have an off by one era. 




"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = [[None] * COLS for row in matrix] 

        def dfs(r, c):
            if dp[r][c] is not None:
                return dp[r][c]
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS:
                    if matrix[nr][nc] > matrix[r][c]:

                        res = max(res, 1 + dfs(nr, nc))
            dp[r][c] = res
            return res

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))

        return res

        