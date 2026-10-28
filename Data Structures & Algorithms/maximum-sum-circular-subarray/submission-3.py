class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Case 1: In the middle
        c1_max = nums[0]
        curmax = 0
        total_sum = sum(nums)
        c2_min = nums[0]
        curmin = 0
        
        for n in nums:
            curmax = max(n, n + curmax)
            c1_max = max(curmax, c1_max)
            curmin = min(n, n + curmin)
            c2_min = min(curmin, c2_min)

        if c1_max < 0:
            return c1_max
        return max(c1_max, total_sum - c2_min)