class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        streak = 0
        maxf = 0
        count = {w:0 for w in set(s)}

        while r < len(s):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            streak = max(streak, r-l+1)
            r += 1        
        return streak