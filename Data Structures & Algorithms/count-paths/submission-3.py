class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prevRow = [0] * (n+1)
        prevRow[n-1] = 1

        for r in range(m-1, -1, -1):
            curRow = [0] * (n+1)
            for c in range(n-1, -1, -1):
                curRow[c] = prevRow[c] + curRow[c+1]
            prevRow = curRow
        
        return prevRow[0]

        