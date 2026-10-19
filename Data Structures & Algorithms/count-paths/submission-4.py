class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0]*(n+1)
        for i in range(m-1, -1, -1):
            curRow = [0]*(n+1)
            curRow[n-1] = 1 if i == m - 1 else 0
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1:
                    curRow[j] = 1
                else:
                    curRow[j] = prevRow[j] + curRow[j+1]
            
            prevRow = curRow

        return prevRow[0]
