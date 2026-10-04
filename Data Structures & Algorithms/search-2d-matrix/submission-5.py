class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = 0
        for r in range(rows):
            if target >= matrix[r][0] and target <= matrix[r][cols-1]:
                row = r
                break
            
        search = matrix[row]
        l, r = 0, cols-1
        while l <= r:
            m = (l + r)//2
            if target == search[m]:
                return True
            if target < search[m]:
                r = m-1
            else:
                l = m+1
        return False
