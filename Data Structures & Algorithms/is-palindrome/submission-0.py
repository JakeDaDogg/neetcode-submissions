class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r: 
            while l < r and not self.conversion(s[l]):
                 l += 1
                 #print(s[l])
            while l < r and not self.conversion(s[r]):
                 r -= 1
                 #print(s[r])
            if s[l].lower()!= s[r].lower():
                return False
            l, r = l + 1, r - 1
            
        return True
    
    def conversion(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        