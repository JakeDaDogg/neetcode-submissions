class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        total = 0
        visit = set()
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque() #rotten
        # find # of fresh fruit in grid
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    total += 1
                elif grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))           

        # bfs
        level = 0
        while q and total > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr >= R or nc >= C or grid[nr][nc] == 0 or (nr, nc) in visit):
                        continue
                    if grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        total -= 1
            level += 1
        
        return level if total == 0 else -1

        # if end of bfs, level of visited !- # of fresh fruit: return -1