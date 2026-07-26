"""
If O cannot reach the outer edges of the board we switch it to board.

In graph/grid questions such as these, we need to 'search' for a path from the O cell to 
the outer.

There are two search algorithms

BFS (breadth first search) and DFS(depth first search)

We are going to use DFS in our solution, becaues DFS is concerned with finding a connection between any two nodes
by exploring in different directions.

Our strategy may look something like this:

We start a DFS from each O, however if we cannot leave the board from that O, we move onto the next, turning that O into an X.
We cannot use use dfs to search through Xs. 

In the end, this will change the board in-place to X's, however what if we eventually reach a solution such as if the X was missing.
We change the visited set() all back to O, whilst making sure they stay within the visited set, so that we don't have
to call DFS on it again.


A better solution is not to go from the inside. The better pattern is to go from the outside.


"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(r, c): #DFS we only call on border O cells
            board[r][c] = 'T' #we have approved this one as True.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0<=nr< ROWS and 0<=nc<COLS): #if next is within boundary
                    # we check if X to see if we call DFS on next Os
                    if board[nr][nc] == 'O':
                        dfs(nr, nc)

        
        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][COLS-1] == 'O':
                dfs(i, COLS - 1)
        for j in range(COLS):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[ROWS-1][j] == 'O':
                dfs(ROWS - 1, j)

        for i in range(ROWS):
            for j in range(COLS):  
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
           




