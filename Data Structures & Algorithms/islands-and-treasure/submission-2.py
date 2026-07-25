from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        INF = 2147483647
        
        def bfs(r, c):
            
            q = deque([(r, c)])
            visit = set()
            visit.add((r, c))
            steps = 0


            while q:

                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and (nr, nc) not in visit):
                            q.append((nr, nc))
                            visit.add((nr, nc))
                steps += 1

            return INF



        
        for i in range(ROWS):

            for j in range(COLS):

                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)


            