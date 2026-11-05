class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for v, d, w in times:
            adj[v].append([d, w])
        
        shortest = {}

        minheap = [[0, k]]

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            
            if n1 in shortest:
                continue
            
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                heapq.heappush(minheap, [w2 + w1, n2])

        for i in range(1, n+1):
            if i not in shortest:
                return -1
        
        return max(shortest.values())