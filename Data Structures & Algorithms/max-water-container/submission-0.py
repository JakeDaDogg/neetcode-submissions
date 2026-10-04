class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            lh, rh = heights[l], heights[r]
            res = max(res, min(lh, rh)*(r-l))
            if rh < lh:
                r -= 1
            else: 
                l += 1
        return res