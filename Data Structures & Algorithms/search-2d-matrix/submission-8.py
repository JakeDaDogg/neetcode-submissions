class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, t = 0, len(matrix) - 1

        row = 0

        while b <= t:
            row = b + (t - b) // 2
            if target < matrix[row][0]:
                t = row - 1
            elif target > matrix[row][-1]:
                b = row + 1
            else:
                break

        if b > t:
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
