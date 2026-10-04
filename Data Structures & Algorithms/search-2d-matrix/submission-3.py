class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0])-1
        m = (l+r)//2

        while l <= r:
            mr = m//len(matrix[0])
            mc = m%len(matrix[0])
            if target < matrix[mr][mc]:
                r = m - 1
            elif target > matrix[mr][mc]:
                l = m + 1
            else:
                return True
            
            m = (l+r)//2
        
        return False
        