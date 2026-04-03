class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
         
        l = 0 
        r = n * len(matrix) - 1

        def findCoordinates(index):
            row = index // n
            col = index % n
            return (row, col)


        while l <= r:
            mid = (r + l) // 2
            x, y = findCoordinates(mid)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False