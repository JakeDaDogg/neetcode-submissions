class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stk = []
        for c in s:
            if c in dic.values():
                stk.append(c)
            else:
                if stk:
                    if dic[c] == stk[-1]:
                        stk.pop()
                    else: return False
                else:
                    return False

        if not stk:
            return True
        else:
            return False