class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        res = []
        dq = deque(nums)
        
        def dfs(dq, cur):
            if not dq:
                res.append(cur.copy())
                return

            for i in range(len(dq)):
                num = dq.popleft()
                cur.append(num)
                dfs(dq, cur)
                cur.pop()
                dq.append(num)
            
        dfs(dq, [])
        return res
            
            


        