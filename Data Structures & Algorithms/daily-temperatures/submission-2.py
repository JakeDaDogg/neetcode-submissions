class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0]*len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            if i == 0:
                stk.append([t, 0])
            else:
                while stk and t > stk[-1][0]:
                    tmp_t, tmp_i = stk.pop()
                    sol[tmp_i] = i - tmp_i
                stk.append([t, i])
        return sol
