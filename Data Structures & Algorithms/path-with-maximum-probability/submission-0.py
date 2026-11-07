class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}

        for i in range(n):
            adj[i] = []
        for i in range(len(succProb)):
            start, end = edges[i]
            weight = succProb[i]
            adj[start].append([weight, end])
            adj[end].append([weight, start])
        
        minheap = [[-1, start_node]]
        paths = {}

        while minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in paths:
                continue
            paths[n1] = abs(w1)

            for w2, n2 in adj[n1]:
                heapq.heappush(minheap, [-1*abs(w2*w1), n2])
            
        return paths[end_node] if end_node in paths else 0




