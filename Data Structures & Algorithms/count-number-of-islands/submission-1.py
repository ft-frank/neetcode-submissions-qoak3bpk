class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0
        cols = len(grid[0]) - 1
        rows= len(grid) - 1
   

        def dfs(row, col):


            if row < 0 or col < 0 or row > rows or col > cols:
                return
            if grid[row][col] == "0" or (row, col) in seen:
                return
            seen.add((row,col))
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)


            

        
        for i in range(rows + 1):

            for j in range(cols + 1):

                if grid[i][j] == "1" and (i, j) not in seen:

                    res += 1
                    dfs(i, j)

        return res
