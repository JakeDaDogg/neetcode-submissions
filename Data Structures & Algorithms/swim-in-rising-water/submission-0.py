class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        minheap = [[grid[0][0], 0, 0]]
        visit.add((0, 0))

        while minheap:
            time, r, c, = heapq.heappop(minheap)
            if r == N-1 and c == N-1:
                return time
            
            for dr, dc in dirs:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 
                    or neiR == N or neiC == N 
                    or (neiR, neiC) in visit):
                    continue
                heapq.heappush(minheap, 
                                [max(time, grid[neiR][neiC]), neiR, neiC])
                visit.add((neiR, neiC))

