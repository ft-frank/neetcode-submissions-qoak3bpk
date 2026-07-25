class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0

        seen = set()

        rows = len(grid) - 1
        cols = len(grid[0]) - 1


        def dfs(row, col):
            

            if row > rows or col > cols or row < 0 or col < 0:
                return 0

            if (row, col) in seen:
                return 0
            seen.add((row, col))   
            if grid[row][col] == 0:
                return 0
            #nitty gritty


            return 1 + (dfs(row  + 1, col)  + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

        for i in range(rows + 1):


            for j in range(cols + 1):


                if grid[i][j] == 1  and (i, j) not in seen:

                    res = max(res, dfs(i, j))
        return res
        #return.....
        
        

