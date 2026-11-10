class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []

        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        res = 0
        minheap = [[0, 0]] 
        visit = set()

        while len(visit) < n and minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in visit:
                continue
            
            res += w1
            visit.add(n1)
            for n2, w2 in adj[n1]:
                heapq.heappush(minheap, [w2, n2])

        return res if len(visit) == n else -1
            
        