class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        rob = [nums[0], max(nums[0],nums[1])]
        
        for i in range(2, len(nums)):
            tmp = rob[1]
            rob[1] = max(nums[i]+rob[0], rob[1])
            rob[0] = tmp

        return max(rob)
            