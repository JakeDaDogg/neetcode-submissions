class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            x, y = p[0], p[1]
            d = -(x**2+y**2)
            heapq.heappush(maxHeap, [d, x, y])
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for item in maxHeap:
            res.append([item[1], item[2]])
        
        return res