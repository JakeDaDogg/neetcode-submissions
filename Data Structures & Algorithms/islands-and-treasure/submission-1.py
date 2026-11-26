class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        q = deque()
        INF = 2147483647

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        def bfs(q):
            level = 1
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF and (nr, nc) not in visit):
                            grid[nr][nc] = level
                            q.append((nr, nc))
                level += 1
            return 
        
        bfs(q)

        
        

        



        


