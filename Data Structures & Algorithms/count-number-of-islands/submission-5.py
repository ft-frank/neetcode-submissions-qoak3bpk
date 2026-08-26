"""
Starting graph revision.



"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = 0

        def dfs(r, c):
            if (r, c) in seen: #alredy seen
                return 
            elif r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0: #outside grid
                return 
            seen.add((r, c)) #mark as seen
            if grid[r][c] == '0': #island continues no longer, return
                return 
            #explore to the right and down.

            for dx, dy in directions:
                dfs(r + dx, c + dy)






        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == '1':
                    dfs(row, col)
                    res += 1


        return res