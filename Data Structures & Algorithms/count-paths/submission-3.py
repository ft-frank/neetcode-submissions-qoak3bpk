"""
Dynamic Programming Question. 

We can do a BFS from the bottom right to be able to determine the possible unique paths in O(m * n) (the number of grid cells), with O(m * n) space.


First, we perform a BFS algorithm starting at the bottom right cell that moves up and to the left, if it is possible
For each cell we travel to using BFS, its possible unique path is equal to the summation of the unique possible paths of the cells
below it and to its right. If these don't exist, then it contributes 0
Continue the BFS algorithm until reaching the top left. We then return dp[(0, 0)]


"""

from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}
        visiting = deque([])
        remaining = {}
        # for r in range(m):
        #     for c in range(n):
        #         #each cell needs 2 cells to exist in dp before they should be added to the array
        #         remaining((r, c)) = (r + 1 < m) + (c + 1 < n) #adding boolean values results in integers. True = 1. False = 0

        #mark the last_cell with 1 unique path

        dp[(m-1,n-1)] = 1
        if n-2 >= 0:
            visiting.append((m-1, n-2))
        if m -2 >= 0:
            visiting.append((m-2, n-1))

        while visiting:
            r, c = visiting.popleft()
            below = dp[(r+1, c)] if (r+1, c) in dp else 0
            to_right = dp[(r, c+1)] if (r, c+1) in dp else 0
            dp[(r, c)] = below + to_right


            if r - 1 >= 0 and (c + 1 >= n or (r-1, c+ 1) in dp):
                visiting.append((r-1, c))
            if c - 1 >= 0 and (r + 1 >= m or (r + 1, c-1) in dp):
                visiting.append((r, c-1))


        return dp[(0, 0)]

        