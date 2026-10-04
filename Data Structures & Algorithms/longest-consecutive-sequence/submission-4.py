class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        res = 1
        cur = 1

        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        
        return res
