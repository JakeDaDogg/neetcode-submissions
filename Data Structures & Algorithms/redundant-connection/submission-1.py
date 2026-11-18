class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}
        
        for u in range(1, len(edges)+1):
            par[u] = u
            rank[u] = 0
        
        def find(u):
            if par[u] != u:
                par[u] = find(par[u])
            return par[u]
        
        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1

            return False

        sol = []
        for u, v in edges:
            if union(u, v):
                sol = [u, v]
            
        return sol