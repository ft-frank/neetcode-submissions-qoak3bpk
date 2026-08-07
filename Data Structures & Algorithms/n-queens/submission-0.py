"""
Backtracking problem. 

1. Have an array of all coordinates. Loop through each coordinate.
2. Place a queen at each coordinate. For that specific scenario, exclude all coordinates
that a queen cannot be placed. Then for the remaining coordinates, loop through them to place another queen.
Do this until there are no more coordinates left, then append to res.

Some concerns:

We will create a n x n array. But we will have to join every n element, to return a valid output.
How to determine if a queen is diagonally attacking a square?

New Way:

3 types of spots.
A O, means an open spot. A . means a spot where we can't place another queen. A Q, means a queen
We loop through each O, placing a Queen there. We then use a function
to turn spots where we can't place queen into a dot.
Then we run dfs on that new board. We then backtrack and then turn the board back to how it was before, 
before investigating another place to put a queen.
We return the board when we have placed n queens

Much easier in a matrix actually....

"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        starting = [["O"] * n for _ in range(n)] #n x n matrix

        # def coordinates(index):
        #     row = index // n
        #     col = index % n
        #     return row, col

        def invalidate(board, r, c):
            return_board = [row.copy() for row in board]

            for k in range(n):
                return_board[r][k] = "."
            for k in range(n):
                return_board[k][c] = "."
            
            #diagonal now. Explore in all 4 directions

            a, b = r, c
            while 0 <= a < n and 0<=b<n:
                return_board[a][b] = "."
                a += 1
                b += 1

            a, b = r, c
            while 0 <= a < n and 0<=b<n:
                return_board[a][b] = "."
                a += 1
                b -= 1

            a, b = r, c
            while 0 <= a < n and 0<=b<n:
                return_board[a][b] = "."
                a -= 1
                b += 1

            a, b = r, c
            while 0 <= a < n and 0<=b<n:
                return_board[a][b] = "."
                a -= 1
                b -= 1

            #turn back into queen
            return_board[r][c] = "Q"
            return return_board
          

            


            
        def dfs(board, queens, row):
            nonlocal res
            if queens == n:
                res_board = ["".join(row) for row in board]
                res.append(res_board)
                return 
            for j in range(n):
                if board[row][j] == "O":
                    board[row][j] = "Q"
                    new_board = invalidate(board, row, j)
                    dfs(new_board, queens + 1, row + 1)
                    board[row][j] = "O"

    

        dfs(starting, 0, 0)
        return res
