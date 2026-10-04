class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stk = []
        dih = ['+', '-', '*', '/']
        for t in tokens:
            if t not in dih:
                stk.append(int(t))
            else:
                second = int(stk.pop())
                first = int(stk.pop())
                if t == '+':
                    new_num = first + second
                if t == '-':
                    new_num = first - second
                if t == '*':
                    new_num = first * second
                if t == '/':
                    new_num = first / second
                stk.append(int(new_num))

        return stk[-1]
