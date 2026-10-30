class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        if len(s) >= 1:
            for i in range(1, len(s)):
                l, r = i-1, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
        
        return res
            