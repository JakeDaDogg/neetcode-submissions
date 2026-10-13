class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n):    
            nxt = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = nxt
        
        return dp[1]