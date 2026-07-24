"""
Recursive backtracking algorithm


We have a recursive function that takes in the index its looking for.

For example dfs(0) is looking for index 0

Then we also have x, y coordinates

dfs(0, 0, 0) looking at A.
In the specific case of 0
we are just looking for first character we move left to right top to bottom to search for first character

Once find first character, then we have an algorithm that can call the recursive function on the coordinate around its
for example 1

dfs (1, 1, 2) is looking at A. Since they match, it recursively calls it again. for the coordinates around it.
Once we have approved index of len(word) - 1. we return True

Return false if all paths have been explored and its false.

Problem is same cell cannot be used more than once.

So we also have to eliminate the cells that we have been to before, probably keep in an array with coordinates before,
or jus 


"""



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        seen = set()
        res = False
        def dfs(i, row, col):
            nonlocal res

            if i >= len(word) - 1:
                res = True
                return

            seen.add((row, col))
            
            if row > 0: #check if next character matches next block
                above = board[row - 1][col]
                if (row - 1, col) not in seen and above == word[i + 1]: #take decision to go up
                   dfs(i + 1, row - 1, col)


            #look right
            if col < cols - 1:
                right = board[row][col + 1]
                if (row, col + 1) not in seen and right == word[i + 1]:
                    dfs(i + 1, row, col + 1)


            #look down
            if row < rows - 1:
                down = board[row + 1][col]
                if  (row + 1, col) not in seen and down == word[i + 1]:
                    dfs(i+1, row + 1, col)


            #look left
            if col > 0:
                left = board[row][col - 1]
                if (row, col - 1) not in seen and left == word[i + 1]:
                    dfs(i+1, row, col - 1)


            seen.remove((row, col))

        for i in range(rows):

            for j in range(cols):

                if board[i][j] == word[0]:

                    dfs(0, i, j)
                    
        return res



