"""

We run a BFS algorithm on each of the preexisting rotten fruits. We start with a queue 
of preexisting fruits. For each minute, 
from each rotten fruit we explore each direction (up, down ,left, right), and identify if it is another rotten fruit, empty or a fresh fruit. If it empty or another rotten fruit or seen. If it is a new rotten fruit, append it to the end of a new queue.

Once the queue becomes empty on a new one, we return the time. 

Then we have to check each and every cell for a fresh fruit.

If none, return time, if still fresh, return -1.

"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        fresh_fruit = 0
        time = 0
        rotted = False
        #don't need a seen, if it is rotten it is seen.
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j)) #r, c indicates the coordinates of rotten fruit
                elif grid[i][j] == 1:
                    fresh_fruit += 1


        while queue: #stops when theres no rotten fruit to explore
            next_queue = deque()
            for r, c in queue: #for each rotten element in queue
                for dr, dc in directions: #explore each direction
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]): #if outside grid
                        continue
                    elif grid[nr][nc] == 0 or grid[nr][nc] == 2: #if seen already, or empty
                        continue
                    
                    #now grid[nr][nc] is def 1
                    
                    grid[nr][nc] = 2 #change to rotten
                    fresh_fruit -= 1
                    rotted = True
                    next_queue.append((nr, nc)) #this rotten we explore its adjacent next time
            if rotted:
                time += 1
            rotted = False
            queue = next_queue


        if fresh_fruit == 0:
            return time
        return -1
"""
On final rotten fruit, if theres no fruit that were rotted, it was not necessary time

"""


        


        
        