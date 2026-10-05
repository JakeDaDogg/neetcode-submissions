class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0]*len(height)
        r = [0]*len(height)
        sol = 0

        for i in range(len(height)):
            if i == 0:
                l[i] = height[i]
            else:
                l[i] = max(height[i], l[i-1])
        
        
        for i in range(1, len(height) + 1):
            if i == 1:
                r[-i] = height[-i]
            else:
                r[-i] = max(height[-i], r[-i+1])
        
        
        for i in range(len(height)):
            sol += min(r[i], l[i]) - height[i]
        
        return sol