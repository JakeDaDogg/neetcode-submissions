class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for w in tokens:
            if w == '+':
                a, b = stk.pop(), stk.pop()
                stk.append(b + a)
            elif w == '-':
                a, b = stk.pop(), stk.pop()
                stk.append(b - a)
            elif w == '*':
                a, b = stk.pop(), stk.pop()
                stk.append(b * a)
            elif w == '/':
                a, b = stk.pop(), stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(w))
        return stk[0]