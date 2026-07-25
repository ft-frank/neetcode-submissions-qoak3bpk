"""
Has to be multisource BFS.

State is impossible if fresh fruit are isolated.
Before running any BFS, we should check if there are any isolated fresh fruit groups, which do not have any fruit around it.
A naive way could be to run DFS on each fresh fruit to make sure it connects to a rotten fruit, and if not return -1.

Then we run BFS from each rotten fruit, which infects each fresh fruit it encounters, finally returning minutes necessary
for q to empty out

OR 
We run BFS from each fresh banana. Once all fresh banana reach a rotten banana we end.

If a fresh banana never reaches a rotten banana, we return -1




"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        minutes = 0

        def bfs():
            nonlocal minutes
            q = deque()
            rotted = False

            for i in range(ROWS):

                for j in range(COLS):

                    if grid[i][j] == 2:
                        q.append((i, j)) #add rotten bananas to cycle

            while q:
                rotted = False
                for _ in range(len(q)):
                    
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0<= nc < COLS and grid[nr][nc] != 0 and grid[nr][nc] != 2):
                            if grid[nr][nc] == 1:
                                rotted = True
                                grid[nr][nc] = 2
                                q.append((nr, nc))
                if rotted:
                    minutes += 1
        bfs()
        for i in range(ROWS):

            for j in range(COLS):

                if grid[i][j] == 1:
                    return -1

        return minutes






