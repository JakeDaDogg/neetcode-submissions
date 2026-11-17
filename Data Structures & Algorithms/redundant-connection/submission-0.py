class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = {}
        rank = {}

        for i in range(1, len(edges)+1):
            par[i] = i
            rank[i] = 0
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            else:
                par[p1] = p2
                rank[p2] += 1
            
            return True

        sol = []
        for u, v in edges:
            if not union(u, v):
                sol = [u, v]
        
        return sol
        

    