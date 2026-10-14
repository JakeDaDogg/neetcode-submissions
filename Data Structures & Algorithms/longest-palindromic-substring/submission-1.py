class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        res = s[0]
        reslen = 1
        for i in range(len(s)):
            odd = self.expand(s, i-1, i+1)
            even = self.expand(s, i, i+1)
            curmax = odd if len(odd) >= len(even) else even
            if len(curmax) >= len(res):
                res = curmax
        return res

        
    def expand(self, s, left, right):
        cur = ''
        while left >= 0 and right < len(s) and s[left] == s[right]:
            cur = s[left:right+1]
        
            left -= 1
            right += 1
    
        return cur
