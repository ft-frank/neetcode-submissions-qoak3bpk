"""

"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        ROWS = len(heights)
        COLS = len(heights[0])

        
        pac = set()
        atl = set()

        
        def dfs(r, c, ocean):
            
            ocean.add((r, c)) #ocean is the set passed through

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS): #if new direction headed in is a valid location
                    if (nr, nc) not in ocean:
                        if heights[nr][nc] >= heights[r][c]:
                            dfs(nr, nc, ocean)

        
        #for the pacific. Column 0, and row 0

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
                    


            



           
            