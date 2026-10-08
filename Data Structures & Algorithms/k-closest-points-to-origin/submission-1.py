class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        heapq.heapify(heap)
        sol = [] #[[x, y]]

        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, [x, y]))
        
        for i in range(k):
            sol.append(heapq.heappop(heap)[1])
        
        return sol
        