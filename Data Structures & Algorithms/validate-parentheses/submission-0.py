class Solution:
    def isValid(self, s: str) -> bool:
        dih = {')':'(', '}':'{', ']':'['}
        stk = []
        for w in s:
            if stk and stk[-1] == dih.get(w):
                stk.pop()
            else:
                stk.append(w)
        
        if not stk:
            return True
        else:
            return False