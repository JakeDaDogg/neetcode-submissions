class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = max(len(text1), len(text2))
        cols = min(len(text1), len(text2))
        long = text2 if len(text2) >= len(text1) else text1
        short = text2 if len(text2) < len(text1) else text1

        prevRow = [0]*(cols+1)

        for r in range(rows):
            curRow = [0]*(cols+1)
            char = long[r]
            for c in range(1, cols+1):
                if short[c-1] == char:
                    curRow[c] += prevRow[c-1] + 1
                else:
                    curRow[c] = max(prevRow[c], curRow[c-1])

            prevRow = curRow
        
        return prevRow[-1]

