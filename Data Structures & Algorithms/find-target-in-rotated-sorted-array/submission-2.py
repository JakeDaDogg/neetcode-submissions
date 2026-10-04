class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        cut = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if m + 1 < len(nums) and nums[m+1] < nums[m]:
                cut = m
                break
            elif nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m - 1

        if nums[0] <= target <= nums[cut]:
            l, r = 0, cut
        else: 
            l, r = cut+1, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1
