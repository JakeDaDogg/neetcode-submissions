class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        tmp = s[l:r]

        while r < len(s):
            tmpset = set(tmp)
            while s[r] in tmpset:
                tmp = tmp[1:]
                l += 1
                tmpset = set(tmp)
            tmp = tmp + s[r]
            res = max(res, len(tmp))
            r += 1
        
        return res
