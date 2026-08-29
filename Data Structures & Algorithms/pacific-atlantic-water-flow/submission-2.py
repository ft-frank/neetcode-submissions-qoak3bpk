"""

DFS from the edge cells.

From an edge cell, attempt to spread to all cells greater than it. If a cell is reached, it is added
to atlantic or pacific.

There will be repeating of corner nodes, but thats negligible, only 4 total.

Then return the intersection of the sets. 


"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        
        pac = set()
        atl = set()
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]


        
        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return

            ocean.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= len(heights) or nc >= len(heights[0]) or (nr, nc) in ocean:
                    continue
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean)
                

            
        
        #pac

        ROWS = len(heights)
        COLS = len(heights[0])


        for i in range(ROWS):
            dfs(i, 0, pac)
        for j in range(COLS):
            dfs(0, j, pac)

        for i in range(ROWS):
            dfs(i, COLS - 1, atl)
        for j in range(COLS):
            dfs(ROWS - 1, j, atl)


        res = pac & atl

        res = list(res)

        res = [[r[0], r[1]] for r in res]
            
        return res


            

            
            

        

            