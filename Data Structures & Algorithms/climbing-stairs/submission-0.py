class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            
        return dp[1]