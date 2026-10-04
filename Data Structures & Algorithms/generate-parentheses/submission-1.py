class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        def dfs(l, r, s):
            if l == r == n:
                sol.append(s)
                return
            
            if l < n:
                dfs(l+1, r, s + '(')
            
            if r < l:
                dfs(l, r+1, s + ')')
        
        dfs(0, 0, '')
        return sol
