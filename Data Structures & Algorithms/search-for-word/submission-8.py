"""

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        ROWS = len(board)
        COLS = len(board[0])
        res = False
        directions = [[1, 0], [0, 1], [-1 , 0], [0, -1]]

        def dfs(i, r, c):
            nonlocal res
            if i >= len(word) - 1: #already found past last character
                res = True
                return
            visited.add((r, c))
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0<=nc<COLS and (nr, nc) not in visited and board[nr][nc] == word[i + 1]):
                    dfs(i + 1, nr, nc)
                    
                 #search in every direction for the next character
            visited.remove((r, c)) #backtrack

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    dfs(0, i, j)
        return res


                

