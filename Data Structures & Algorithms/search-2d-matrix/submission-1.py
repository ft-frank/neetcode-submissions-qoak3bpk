class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = (rows * cols) - 1

        while l <= r:
            mid_index = (l + r) // 2
            mid_row = mid_index // cols
            mid_col = mid_index % cols
            value = matrix[mid_row][mid_col]
            if value == target:
                return True
            elif target > value:
                l = mid_index + 1
            else:
                r = mid_index - 1
        return False







