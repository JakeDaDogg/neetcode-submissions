class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        prevRow = [0]*(cols+1)
        prevRow[cols-1] = 1
        
        for r in range(rows-1, -1, -1):
            curRow = [0]*(cols+1)

            for c in range(cols-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow
        
        return curRow[0]