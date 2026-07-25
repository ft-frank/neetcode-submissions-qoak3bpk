class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        inspected = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):

            inspected.add((row, col))
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc) not in inspected and
                grid[nr][nc] == '1'):
                    dfs(nr, nc)
                    
                    
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in inspected:
                    res += 1
                    dfs(i, j)
            
        return res
            
	
	
	