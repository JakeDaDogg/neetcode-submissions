class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        if sc != tc:
            return False
        else: return True