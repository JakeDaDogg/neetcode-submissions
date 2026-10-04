class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            # base case:
            if i >= len(nums):
                res.append(subset[:])
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # Decision NOT to include nums[i] and all its duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
            
        
        dfs(0)
        return res

        