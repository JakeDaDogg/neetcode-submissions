class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # set(temp, index)
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                tmp, idx = stack.pop()
                res[idx] = i-idx
            stack.append([temperatures[i], i]) 
        return res