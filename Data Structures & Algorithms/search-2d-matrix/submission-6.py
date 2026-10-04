class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        r = 0
        left, right = 0, cols - 1

        while r + 1 < rows and matrix[r + 1][0] <= target:
            r += 1

        while left <= right:
            m = left + (right - left) // 2
            if matrix[r][m] < target:
                left = m + 1
            elif matrix[r][m] > target:
                right = m - 1
            else:
                return True
        
        return False