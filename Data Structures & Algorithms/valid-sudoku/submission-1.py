class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                elif num in seen:
                    return False
                else:
                    seen.add(num)
        for col in range(9):
            seen = set()
            for row in board:
                if row[col] == ".":
                    continue
                elif row[col] in seen:
                    return False
                else:
                    seen.add(row[col])

        
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)


        return True


        

                




        return True