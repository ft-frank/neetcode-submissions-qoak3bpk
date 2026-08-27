"""
ALGORITHM:

We run a depth-first-search algorithm on each grid block. 
This algorithm traverses, adding 1 to the count for each grid found, exploring all 
blocks adjacent (up, left, down, right)
We then save the maximum between the response and this area.
All the grids we traversed are saved in seen during traversal, because calling dfs on that
grid will result in the same area as calling on another grid within that area.


"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()
    
        

        def dfs(r, c):
            if (r, c) in seen:
                return 0
            elif r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            elif grid[r][c] == 0:
                return 0

            seen.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) +dfs (r, c-1)
            







        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == 1:
                    res = max(dfs(row, col), res)

        return res

