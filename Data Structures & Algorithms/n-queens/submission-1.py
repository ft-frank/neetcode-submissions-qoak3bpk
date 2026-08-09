"""
Backtracking!

1. Call function backtrack, or DFS
2. Most ideally has 1 variable for 1D backtracking.
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        res = []
        board = [['.'] * n for _ in range(n)] #empty n x n matrix 

       



        def backtrack(row):
            if row == n:
                nonlocal res
                res.append(["".join(row) for row in board]) #will put into proper form later
                return 
            for col in range(n):
                #only do something if it safe to put a queen
                if valid(row, col): 
                    board[row][col] = 'Q' #change square on board to Queen
                    backtrack(row + 1) #run algorithm on the next row, with the queen having been placed
                    board[row][col] = "." #remove the Queen


        def valid(r, c): # a function that takes in a coordinate, and then just looks behind for any QUEENS.
            #No need to check within same row, each call is on a next row.

            #check all in column above
            for j in range(0, r): #check all rows above
                if board[j][c] == 'Q':
                    return False

            r1 = r2 = r
            c1 = c2 = c

            #check diagonally up to the left
            while r1 >= 0 and c1 >= 0:
                if board[r1][c1] == 'Q':
                    return False
                r1-=1
                c1-=1

            #check diagonally up to the right.
            while r2 >= 0 and c2 < n:
                if board[r2][c2] == 'Q':
                    return False
                r2-=1
                c2+=1
            return True


        backtrack(0)
        return res  
