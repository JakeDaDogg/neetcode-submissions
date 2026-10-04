class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        arr = [0]*len(position)
        for i in range(len(arr)):
            arr[i] = [position[i], speed[i]]
        
        arr.sort(key=lambda x: x[0], reverse=True)
        for item in arr:
            time = (target-item[0])/item[1]
            if not stk: stk.append(time)
            else:
                if time > stk[-1]:
                    stk.append(time)
        
        return len(stk)
            


