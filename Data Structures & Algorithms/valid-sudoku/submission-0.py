from collections import defaultdict

class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
                
            rows = defaultdict(list)
            cols = defaultdict(list)
            squares = defaultdict(list)

                                               
            for rowPos, row in enumerate(board):
                for col, number in enumerate(row):                                                
                    if number == ".":
                        continue
                    if number in rows[rowPos]:
                        return False
                    rows[rowPos].append(number)

                    if number in cols[col]:
                        return False
                    cols[col].append(number)

                    square = (rowPos // 3, col //3)
                    if number in squares[square]: # there are 9 squares with 3 x 3. Therefore this is a coordinate of the square. I see
                        return False
                    squares[square].append(number)
            return True
        