class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        res, cursum = nums[0], nums[0]
        while r < len(nums) - 1:
            if cursum < 0:
                r += 1
                l = r
                cursum = nums[l]
            else:
                r += 1
                cursum += nums[r]
            res = max(res, cursum)
        
        return res