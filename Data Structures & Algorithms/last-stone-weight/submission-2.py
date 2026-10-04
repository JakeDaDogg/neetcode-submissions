class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            big = heapq.heappop(maxHeap)
            small = heapq.heappop(maxHeap)
            if big - small < 0:
                heapq.heappush(maxHeap, big - small)
        
        heapq.heappush(maxHeap, 0)
        return -maxHeap[0]