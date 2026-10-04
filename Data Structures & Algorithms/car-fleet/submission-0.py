class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            t2 = (target-p)/s
            stack.append(t2)
            if len(stack) > 1 and t2 <= stack[-2]:
                stack.pop()
        return len(stack)
