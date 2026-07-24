class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        seen = set()

        rows = len(grid) - 1
        cols = len(grid[0]) - 1

        res = 0


        def dfs(row, col):

            if row > rows or col > cols or row < 0 or col < 0:
                return
            if (row, col) in seen or grid[row][col] == "0":
                return
            seen.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for i in range(rows + 1):

            for j in range(cols + 1):

                if (i, j) not in seen and grid[i][j] == "1":
                    res +=  1
                    dfs(i, j)

        return res
