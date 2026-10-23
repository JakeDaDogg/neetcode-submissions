class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        else:
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                tmp = max(dp[0] + nums[i], dp[1])
                dp[1], dp[0] = tmp, dp[1]
        
        return dp[1]