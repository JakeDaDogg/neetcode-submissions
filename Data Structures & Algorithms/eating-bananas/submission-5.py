class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = l + (r - l)//2
            time = 0
            for p in piles:
                time += math.ceil(p/m)
            
            if time <= h:
                r = m - 1
                res = min(res, m)
            
            else:
                l = m + 1
        
        return res

